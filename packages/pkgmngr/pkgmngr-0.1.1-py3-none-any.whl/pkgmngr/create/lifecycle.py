"""
Lifecycle management functions for package creation and maintenance.
"""

import os
import subprocess
import shutil
import re
import sys
import toml
import json
import requests
from pathlib import Path
from contextlib import contextmanager
from distutils.spawn import find_executable

from pkgmngr.common.utils import sanitize_package_name
from pkgmngr.common.errors import PackageError, GitError, GithubError, ConfigError, error_handler, try_operation
from pkgmngr.common.cli import display_info, display_success, display_warning, display_error, get_input_with_default
from pkgmngr.common.config import load_config, save_config, get_github_info
from pkgmngr.common.pypi import check_name_availability


@contextmanager
def change_directory(path):
    """
    Context manager for changing the current working directory.
    
    Args:
        path: Path to change to
    """
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)


@error_handler
def rename_project(old_name, new_name, skip_github=False, base_dir=None):
    """
    Rename a project, updating all references to the old name,
    and optionally renaming the GitHub repository.
    
    This function performs a comprehensive scan of the project to replace:
    - The package directory name
    - All occurrences of the old name in file contents
    - All occurrences of the sanitized old name in file contents
    - Files with the old name or sanitized old name in their filename
    
    Args:
        old_name: Current name of the package
        new_name: New name for the package
        skip_github: If True, skip GitHub repository renaming even if token is available
        base_dir: Base directory (default: current directory)
    
    Returns:
        int: 0 if successful, 1 otherwise
    """
    # Check PyPI availability for the new name
    from pkgmngr.common.pypi import check_name_availability
    
    if not check_name_availability(new_name, context="rename"):
        display_info("Rename operation cancelled.")
        return 0
    
    # Use provided base directory or current directory
    base_dir = base_dir or os.getcwd()
    
    # Validate package names and load config
    config, config_path = validate_rename_parameters(old_name, base_dir)
    
    # Create sanitized versions of names
    old_sanitized = sanitize_package_name(old_name)
    new_sanitized = sanitize_package_name(new_name)
    
    # Check if GitHub integration is needed
    github_info = check_github_integration(base_dir, skip_github)
    
    # Update config file
    update_config_file(config, new_name, config_path)
    
    # Rename package directory
    rename_directory(base_dir, old_sanitized, new_sanitized)
    
    # Track renamed files to avoid processing them twice
    renamed_files = set()
    
    # First pass: rename files with old_name or old_sanitized in their names
    renamed_files.update(rename_files_with_pattern(base_dir, old_name, new_name, old_sanitized, new_sanitized))
    
    # Second pass: update content in all files
    update_file_contents_recursively(base_dir, old_name, new_name, old_sanitized, new_sanitized, renamed_files)
    
    # Handle GitHub repository renaming if applicable
    handle_github_rename(github_info, old_name, new_name, base_dir, skip_github)
    
    display_success(f"\nProject successfully renamed from '{old_name}' to '{new_name}'")
    display_info("All references to the old name have been updated.")
    return 0

def rename_directory(base_dir, old_sanitized, new_sanitized):
    """
    Rename the package directory.
    
    Args:
        base_dir: Base directory
        old_sanitized: Sanitized old package name
        new_sanitized: Sanitized new package name
    """
    old_pkg_dir = os.path.join(base_dir, old_sanitized)
    new_pkg_dir = os.path.join(base_dir, new_sanitized)
    
    if os.path.exists(old_pkg_dir) and os.path.isdir(old_pkg_dir):
        if os.path.exists(new_pkg_dir):
            raise PackageError(f"Cannot rename: Directory {new_pkg_dir} already exists")
        os.rename(old_pkg_dir, new_pkg_dir)
        display_info(f"Renamed package directory: {old_sanitized} → {new_sanitized}")

def rename_files_with_pattern(base_dir, old_name, new_name, old_sanitized, new_sanitized):
    """
    Rename all files containing the old name pattern in their filename.
    
    Args:
        base_dir: Base directory
        old_name: Old package name
        new_name: New package name
        old_sanitized: Sanitized old package name
        new_sanitized: Sanitized new package name
        
    Returns:
        Set of paths of renamed files
    """
    renamed_files = set()
    
    for root, dirs, files in os.walk(base_dir):
        # Skip .git directory and any hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Process each file in this directory
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Skip binary files
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Just try to read a bit to see if it's text
                    f.read(4096)
            except (UnicodeDecodeError, IOError):
                continue
            
            # Check if filename contains old_name or old_sanitized
            old_name_in_filename = old_name in filename
            old_sanitized_in_filename = old_sanitized in filename
            
            if old_name_in_filename or old_sanitized_in_filename:
                # Create new filename
                new_filename = filename
                if old_name_in_filename:
                    new_filename = new_filename.replace(old_name, new_name)
                if old_sanitized_in_filename:
                    new_filename = new_filename.replace(old_sanitized, new_sanitized)
                
                # Rename the file
                new_file_path = os.path.join(root, new_filename)
                if not os.path.exists(new_file_path):
                    os.rename(file_path, new_file_path)
                    display_info(f"Renamed file: {file_path} → {new_file_path}")
                    renamed_files.add(new_file_path)
    
    return renamed_files

def update_file_contents_recursively(base_dir, old_name, new_name, old_sanitized, new_sanitized, renamed_files=None):
    """
    Update references to old name and old sanitized name in all text files.
    
    Args:
        base_dir: Base directory
        old_name: Old package name
        new_name: New package name
        old_sanitized: Sanitized old package name
        new_sanitized: Sanitized new package name
        renamed_files: Set of files that have been renamed (to avoid processing them twice)
    """
    if renamed_files is None:
        renamed_files = set()
    
    # Create a counter for modified files
    files_modified = 0
    
    # Extensions to process - add more as needed
    text_extensions = {
        '.py', '.md', '.txt', '.rst', '.json', '.yaml', '.yml', 
        '.toml', '.ini', '.cfg', '.html', '.css', '.js',
        '.sh', '.bat', '.ps1', '.dockerfile', '.svg'
    }
    
    for root, dirs, files in os.walk(base_dir):
        # Skip .git directory and any hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Process each file in this directory
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Skip if this file was already renamed
            if file_path in renamed_files:
                continue
                
            # Skip non-text files and files with extensions we don't care about
            _, ext = os.path.splitext(filename)
            if ext.lower() not in text_extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Just try to read a bit to see if it's text
                        f.read(4096)
                except (UnicodeDecodeError, IOError):
                    continue
            
            # Update file content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if content contains any patterns we need to replace
                original_content = content
                
                # Replace package name
                if old_name in content:
                    content = content.replace(old_name, new_name)
                
                # Replace sanitized package name
                if old_sanitized in content:
                    content = content.replace(old_sanitized, new_sanitized)
                
                # Write content back if modified
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
            except (UnicodeDecodeError, IOError):
                # Skip binary files or files with encoding issues
                continue
    
    display_info(f"Updated content in {files_modified} files")

def validate_rename_parameters(old_name, base_dir):
    """
    Validate package names and load configuration.
    
    Args:
        old_name: Current name of the package
        base_dir: Base directory
        
    Returns:
        Tuple of (config, config_path)
        
    Raises:
        ConfigError: If validation fails
    """
    try:
        config, config_path = load_config(base_dir)
    except FileNotFoundError:
        raise ConfigError("Config file not found in current directory. Run 'pkgmngr new PACKAGE_NAME' first or change to the package directory.")
        
    current_name = config.get("package_name")
    if current_name != old_name:
        raise ConfigError(f"Current package name in config is '{current_name}', not '{old_name}'")
    
    return config, config_path

def rename_package_directory(base_dir, old_sanitized, new_sanitized):
    """
    Rename the package directory.
    
    Args:
        base_dir: Base directory
        old_sanitized: Sanitized old package name
        new_sanitized: Sanitized new package name
    """
    old_pkg_dir = os.path.join(base_dir, old_sanitized)
    new_pkg_dir = os.path.join(base_dir, new_sanitized)
    if os.path.exists(old_pkg_dir) and os.path.isdir(old_pkg_dir):
        os.rename(old_pkg_dir, new_pkg_dir)
        display_info(f"Renamed package directory: {old_sanitized} → {new_sanitized}")

def check_github_integration(base_dir, skip_github):
    """
    Check if GitHub integration is needed and available.
    
    Args:
        base_dir: Base directory
        skip_github: Whether to skip GitHub operations
        
    Returns:
        Dictionary with GitHub information or None if not needed
    """
    # Check if this is a git repository
    is_git_repo = is_git_repository(base_dir)
    if not is_git_repo:
        display_info("Not inside a Git repository. GitHub renaming will be skipped.")
        return None
    
    # If this is a git repo, check if GitHub remote exists
    github_remote_url, github_username = get_github_remote_info(base_dir)
    if github_username:
        display_info(f"Detected GitHub repository: {github_username}/{github_remote_url.split('/')[-1].replace('.git', '')}")
        return {
            "remote_url": github_remote_url,
            "username": github_username
        }
    
    return None


def update_config_file(config, new_name, config_path):
    """
    Update the configuration file with the new package name.
    
    Args:
        config: Configuration dictionary
        new_name: New package name
        config_path: Path to the config file
    """
    config["package_name"] = new_name
    save_config(config, config_path)
    display_info(f"Updated config file with new package name: {new_name}")


def update_test_files(base_dir, old_sanitized, new_sanitized):
    """
    Update test files for the package.
    
    Args:
        base_dir: Base directory
        old_sanitized: Sanitized old package name
        new_sanitized: Sanitized new package name
    """
    test_dir = os.path.join(base_dir, "tests")
    if not os.path.exists(test_dir):
        return
        
    # Rename test file
    old_test_file = os.path.join(test_dir, f"test_{old_sanitized}.py")
    new_test_file = os.path.join(test_dir, f"test_{new_sanitized}.py")
    if os.path.exists(old_test_file):
        os.rename(old_test_file, new_test_file)
        display_info(f"Renamed test file: {old_test_file} → {new_test_file}")
        
    # Update content of test files to use new import
    for test_file in Path(test_dir).glob("*.py"):
        update_file_content(test_file, f"import {old_sanitized}", f"import {new_sanitized}")
        update_file_content(test_file, f"from {old_sanitized}", f"from {new_sanitized}")


def update_setup_py(base_dir, old_name, new_name, old_sanitized, new_sanitized, github_info):
    """
    Update setup.py with the new package name.
    
    Args:
        base_dir: Base directory
        old_name: Old package name
        new_name: New package name
        old_sanitized: Sanitized old package name
        new_sanitized: Sanitized new package name
        github_info: GitHub information dictionary or None
    """
    setup_py = os.path.join(base_dir, "setup.py")
    if not os.path.exists(setup_py):
        return
        
    # Update package name
    update_file_content(setup_py, f'name="{old_name}"', f'name="{new_name}"')
    
    # Update packages list
    update_file_content(setup_py, f'packages=\\["{old_sanitized}"\\]', f'packages=["{new_sanitized}"]')
    
    # Update entry points
    update_file_content(
        setup_py, 
        f'"{old_name}={old_sanitized}', 
        f'"{new_name}={new_sanitized}'
    )
    
    # Update GitHub URL if present
    if github_info and github_info["username"]:
        update_file_content(
            setup_py, 
            f"github.com/{github_info['username']}/{old_name}", 
            f"github.com/{github_info['username']}/{new_name}"
        )


def update_readme(base_dir, old_name, new_name, old_sanitized):
    """
    Update README.md with the new package name.
    
    Args:
        base_dir: Base directory
        old_name: Old package name
        new_name: New package name
        old_sanitized: Sanitized old package name
    """
    readme = os.path.join(base_dir, "README.md")
    if not os.path.exists(readme):
        return
        
    update_file_content(readme, f"# {old_name}", f"# {new_name}")
    update_file_content(readme, f"pip install {old_name}", f"pip install {new_name}")
    update_file_content(readme, f"import {old_sanitized}", f"import {sanitize_package_name(new_name)}")
    
    if old_name != old_sanitized:  # Only do general replacement if sanitized name differs
        update_file_content(readme, old_name, new_name)


def handle_github_rename(github_info, old_name, new_name, base_dir, skip_github):
    """
    Handle GitHub repository renaming if applicable.
    
    Args:
        github_info: GitHub information dictionary or None
        old_name: Old package name
        new_name: New package name
        base_dir: Base directory
        skip_github: Whether to skip GitHub operations
    """
    if not github_info or skip_github:
        return
        
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        success = rename_github_repository(
            github_info["username"], 
            old_name, 
            new_name, 
            github_token, 
            github_info["remote_url"],
            base_dir
        )
        if not success:
            display_warning("Local project renamed successfully, but GitHub repository remains unchanged.")
            display_info("You may need to manually rename the GitHub repository.")
    else:
        display_warning("GITHUB_TOKEN environment variable not set. Skipping GitHub repository renaming.")
        display_info("Local project renamed successfully, but GitHub repository remains unchanged.")
        display_info("To rename the GitHub repository, set the GITHUB_TOKEN environment variable and run:")
        display_info(f"  pkgmngr rename {new_name} {new_name}")


def is_git_repository(base_dir=None):
    """
    Check if the current directory is a Git repository.
    
    Args:
        base_dir: Base directory to check (default: current directory)
        
    Returns:
        bool: True if it's a Git repository, False otherwise
    """
    base_dir = base_dir or os.getcwd()
    
    with change_directory(base_dir):
        try:
            subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False


def get_github_remote_info(base_dir=None):
    """
    Get GitHub remote URL and username from a Git repository.
    
    Args:
        base_dir: Base directory to check (default: current directory)
        
    Returns:
        tuple: (remote_url, username) or (None, None) if not found
    """
    base_dir = base_dir or os.getcwd()
    
    with change_directory(base_dir):
        try:
            # Get remote URL
            remote_url = subprocess.check_output(
                ["git", "remote", "get-url", "origin"],
                stderr=subprocess.PIPE,
                universal_newlines=True
            ).strip()
            
            # Extract username from remote URL
            return extract_github_username(remote_url)
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None, None


def extract_github_username(remote_url):
    """
    Extract GitHub username from a remote URL.
    
    Args:
        remote_url: GitHub remote URL
        
    Returns:
        Tuple of (remote_url, username) or (remote_url, None) if not found
    """
    username = None
    if "github.com" in remote_url:
        if remote_url.startswith("https://"):
            # Format: https://github.com/username/repo.git
            parts = remote_url.split("/")
            if len(parts) >= 4:
                username = parts[3]
        elif remote_url.startswith("git@"):
            # Format: git@github.com:username/repo.git
            parts = remote_url.split(":")
            if len(parts) >= 2:
                username = parts[1].split("/")[0]
    
    return remote_url, username


def rename_github_repository(username, old_name, new_name, token, remote_url, base_dir=None):
    """
    Rename a GitHub repository and update the remote URL.
    
    Args:
        username: GitHub username
        old_name: Current repository name
        new_name: New repository name
        token: GitHub token
        remote_url: Current remote URL
        base_dir: Base directory (default: current directory)
        
    Returns:
        bool: True if successful, False otherwise
    """
    base_dir = base_dir or os.getcwd()
    display_info(f"Renaming GitHub repository from {old_name} to {new_name}...")
    
    success = github_api_rename_repo(username, old_name, new_name, token)
    if not success:
        return False
    
    # Update git remote URL
    new_remote_url = generate_new_remote_url(remote_url, old_name, new_name)
    update_git_remote(base_dir, new_remote_url)
    
    return True


def github_api_rename_repo(username, old_name, new_name, token):
    """
    Use GitHub API to rename a repository.
    
    Args:
        username: GitHub username
        old_name: Current repository name
        new_name: New repository name
        token: GitHub token
        
    Returns:
        bool: True if successful, False otherwise
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "name": new_name
    }
    
    try:
        response = requests.patch(
            f"https://api.github.com/repos/{username}/{old_name}",
            headers=headers,
            data=json.dumps(data)
        )
        
        if response.status_code == 200:
            display_success(f"Successfully renamed GitHub repository to {username}/{new_name}")
            return True
        else:
            error_msg = response.json().get('message', 'Unknown error')
            raise GithubError(f"Failed to rename GitHub repository: {error_msg}")
    except Exception as e:
        display_error(f"Error renaming GitHub repository: {str(e)}")
        return False


def generate_new_remote_url(remote_url, old_name, new_name):
    """
    Generate a new remote URL with the new repository name.
    
    Args:
        remote_url: Current remote URL
        old_name: Current repository name
        new_name: New repository name
        
    Returns:
        New remote URL
    """
    if "https://" in remote_url:
        return remote_url.replace(f"/{old_name}.git", f"/{new_name}.git")
    else:  # SSH format
        return remote_url.replace(f"/{old_name}.git", f"/{new_name}.git")


def update_git_remote(base_dir, new_remote_url):
    """
    Update Git remote URL.
    
    Args:
        base_dir: Base directory
        new_remote_url: New remote URL
    """
    with change_directory(base_dir):
        # Set the new remote URL
        try_operation(
            lambda: subprocess.run(
                ["git", "remote", "set-url", "origin", new_remote_url],
                check=True,
                stdout=subprocess.PIPE
            ),
            f"Failed to update Git remote URL",
            GitError
        )
        display_info(f"Updated git remote URL to {new_remote_url}")


@error_handler
def dump_to_github(base_dir=None):
    """
    Commit all changes and push to GitHub.
    
    Args:
        base_dir: Base directory (default: current directory)
    
    Returns:
        int: 0 if successful, 1 otherwise
    """
    base_dir = base_dir or os.getcwd()
    
    # Check if inside a Git repository
    if not is_git_repository(base_dir):
        raise GitError("Not inside a Git repository. Run 'pkgmngr create init-repo' first to initialize Git")
    
    # Ask for commit message
    display_info("Enter a commit message:")
    commit_message = input("> ").strip()
    if not commit_message:
        commit_message = "Update package files"
    
    with change_directory(base_dir):
        return execute_git_operations(commit_message)


def execute_git_operations(commit_message):
    """
    Execute Git operations (add, commit, push).
    
    Args:
        commit_message: Commit message
        
    Returns:
        int: 0 if successful, 1 otherwise
        
    Raises:
        GitError: If Git operations fail
    """
    # Check if there are changes to commit
    status_output = check_git_status()
    if not status_output:
        display_info("No changes to commit")
        return 0
    
    # Add all changes
    add_changes_to_git()
    
    # Commit changes
    commit_changes(commit_message)
    
    # Push to remote
    push_changes_to_remote()
    
    return 0


def check_git_status():
    """
    Check Git status to see if there are changes.
    
    Returns:
        Status output or empty string if no changes
    """
    status_output = subprocess.check_output(
        ["git", "status", "--porcelain"],
        universal_newlines=True
    )
    return status_output.strip()


def add_changes_to_git():
    """
    Add all changes to Git staging area.
    
    Raises:
        GitError: If adding changes fails
    """
    try_operation(
        lambda: subprocess.run(["git", "add", "."], check=True),
        "Failed to add changes to Git staging area",
        GitError
    )
    display_info("Added all changes to staging area")


def commit_changes(commit_message):
    """
    Commit changes to Git.
    
    Args:
        commit_message: Commit message
        
    Raises:
        GitError: If committing changes fails
    """
    try_operation(
        lambda: subprocess.run(["git", "commit", "-m", commit_message], check=True),
        "Failed to commit changes",
        GitError
    )
    display_info(f"Committed changes with message: '{commit_message}'")


def push_changes_to_remote():
    """
    Push changes to remote Git repository.
    
    Raises:
        GitError: If pushing changes fails
    """
    # Get current branch
    current_branch = subprocess.check_output(
        ["git", "branch", "--show-current"],
        universal_newlines=True
    ).strip()
    
    try_operation(
        lambda: subprocess.run(["git", "push", "origin", current_branch], check=True),
        f"Failed to push changes to GitHub branch '{current_branch}'",
        GitError
    )
    display_success(f"Pushed changes to GitHub (branch: {current_branch})")


@error_handler
def upload_to_pypi(test=False, base_dir=None):
    """
    Build and upload the package to PyPI or TestPyPI.
    
    Args:
        test: If True, upload to TestPyPI instead of PyPI
        base_dir: Base directory (default: current directory)
    
    Returns:
        int: 0 if successful, 1 otherwise
    """
    base_dir = base_dir or os.getcwd()
    
    # Check if necessary tools are installed
    verify_required_tools()
    
    with change_directory(base_dir):
        # Clean, build and upload
        clean_build_artifacts()
        build_package()
        upload_package(test, base_dir)
        
        return 0

def find_python_executable():
    """
    Find the appropriate Python executable.
    Tries python, python3, and sys.executable in that order.
    
    Returns:
        str: Path to the Python executable
    
    Raises:
        PackageError: If no Python executable can be found
    """
    # First, try the current Python executable (from sys.executable)
    # This is most likely to be the correct one, especially in a virtual environment
    if sys.executable and os.path.exists(sys.executable):
        return sys.executable
    
    # Try common Python executable names
    for executable in ["python", "python3"]:
        if find_executable(executable):
            return executable
    
    # If we get here, we couldn't find a Python executable
    raise PackageError("No Python executable found. Please make sure Python is in your PATH.")

def verify_required_tools():
    """
    Verify that required tools are installed.
    
    Raises:
        PackageError: If required tools are missing
    """
    # Check for Python executable
    try:
        python_exe = find_python_executable()
    except PackageError as e:
        raise e
    
    # Check for pip and twine as modules rather than executables
    # Since we'll use them with the Python executable we found
    try:
        subprocess.run(
            [python_exe, "-m", "pip", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError:
        raise PackageError("pip module not found. Please install pip and try again")
    
    try:
        subprocess.run(
            [python_exe, "-m", "twine", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError:
        raise PackageError("twine module not found. Please install twine using 'pip install twine' and try again")


def clean_build_artifacts():
    """
    Clean up any existing build artifacts.
    
    Raises:
        PackageError: If cleanup fails
    """
    try:
        for directory in ["build", "dist", "*.egg-info"]:
            for path in Path(".").glob(directory):
                if path.is_dir():
                    shutil.rmtree(path)
                    display_info(f"Removed directory: {path}")
    except Exception as e:
        raise PackageError(f"Failed to clean build artifacts: {str(e)}")


def build_package():
    """
    Build the Python package.
    
    Raises:
        PackageError: If building the package fails
    """
    display_info("Building package...")
    python_exe = find_python_executable()
    
    try_operation(
        lambda: subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "build"], check=True),
        "Failed to install build package",
        PackageError
    )
    
    try_operation(
        lambda: subprocess.run([python_exe, "-m", "build"], check=True),
        "Failed to build package",
        PackageError
    )


def upload_package(test, base_dir):
    """
    Upload the package to PyPI or TestPyPI.
    
    Args:
        test: If True, upload to TestPyPI
        base_dir: Base directory
        
    Raises:
        PackageError: If uploading fails
    """
    if test:
        # Upload to TestPyPI
        upload_to_test_pypi(base_dir)
    else:
        # Upload to PyPI
        upload_to_real_pypi()


def upload_to_test_pypi(base_dir):
    """
    Upload to TestPyPI and display instructions.
    
    Args:
        base_dir: Base directory
        
    Raises:
        PackageError: If uploading fails
    """
    display_info("Uploading to TestPyPI...")
    python_exe = find_python_executable()
    
    try_operation(
        lambda: subprocess.run([
            python_exe, "-m", "twine", "upload", "--repository-url", "https://test.pypi.org/legacy/", "dist/*"
        ], check=True),
        "Failed to upload to TestPyPI",
        PackageError
    )
    
    # Get package name from config
    config, _ = load_config(base_dir)
    package_name = config.get("package_name")
    
    display_success("\nPackage uploaded to TestPyPI successfully!")
    display_info(f"You can install it with:")
    display_info(f"pip install --index-url https://test.pypi.org/simple/ {package_name}")


def upload_to_real_pypi():
    """
    Upload to PyPI.
    
    Raises:
        PackageError: If uploading fails
    """
    display_info("Uploading to PyPI...")
    python_exe = find_python_executable()
    
    try_operation(
        lambda: subprocess.run([python_exe, "-m", "twine", "upload", "dist/*"], check=True),
        "Failed to upload to PyPI",
        PackageError
    )
    display_success("\nPackage uploaded to PyPI successfully!")


def update_file_content(file_path, pattern, replacement):
    """
    Update content in a file based on a pattern.
    
    Args:
        file_path: Path to the file
        pattern: Regex pattern to search for
        replacement: Replacement string
        
    Raises:
        PackageError: If updating file content fails
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated_content = re.sub(pattern, replacement, content)
        
        if content != updated_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            display_info(f"Updated references in {file_path}")
    except Exception as e:
        raise PackageError(f"Failed to update file content in {file_path}: {str(e)}")