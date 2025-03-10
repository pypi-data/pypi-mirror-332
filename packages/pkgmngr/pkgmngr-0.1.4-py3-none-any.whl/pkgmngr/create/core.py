"""
Core functionality for creating Python package structures.
"""
import os
from pathlib import Path

from pkgmngr.common.templates import render_template
from pkgmngr.common.utils import create_file, create_directory, sanitize_package_name
from pkgmngr.common.errors import PackageError, try_operation, assert_condition


def create_package_structure(package_name, author="Your Name", year="2025", github_username=None):
    """
    Create a package structure for a new Python package.
    
    Args:
        package_name: Name of the package
        author: Author of the package
        year: Year for the license
        github_username: GitHub username (optional)
        
    Raises:
        PackageError: If package creation fails
    """
    try:
        # Validate inputs
        validate_package_inputs(package_name, author, year)
        
        # Create sanitized package name (Python compatible)
        sanitized_name = sanitize_package_name(package_name)
        
        # Use current directory as root
        root_dir = Path(".")
        
        # If github_username is not provided, use a placeholder
        github_username = github_username or "username"
        
        # Create directory structure
        package_dir, tests_dir = create_package_directories(root_dir, sanitized_name)
        
        # Create package files
        create_package_files(root_dir, sanitized_name, package_name, author, year, github_username)
        
        # Print summary
        print_creation_summary(sanitized_name)
        
    except Exception as e:
        if isinstance(e, PackageError):
            raise e
        else:
            raise PackageError(f"Failed to create package structure: {str(e)}")


def validate_package_inputs(package_name, author, year):
    """
    Validate inputs for package creation.
    
    Args:
        package_name: Name of the package
        author: Author of the package
        year: Year for the license
        
    Raises:
        PackageError: If inputs are invalid
    """
    assert_condition(
        package_name and isinstance(package_name, str),
        "Package name must be a non-empty string",
        PackageError
    )
    
    assert_condition(
        author and isinstance(author, str),
        "Author name must be a non-empty string",
        PackageError
    )
    
    assert_condition(
        year and isinstance(year, str),
        "Year must be a non-empty string",
        PackageError
    )


def create_package_directories(root_dir, sanitized_name):
    """
    Create the necessary directories for the package.
    
    Args:
        root_dir: Root directory path
        sanitized_name: Sanitized package name
        
    Returns:
        Tuple of (package_dir, tests_dir)
        
    Raises:
        PackageError: If directory creation fails
    """
    try:
        # Create package directory
        package_dir = root_dir / sanitized_name
        create_directory(package_dir)
        
        # Create tests directory
        tests_dir = root_dir / "tests"
        create_directory(tests_dir)
        
        return package_dir, tests_dir
    except Exception as e:
        raise PackageError(f"Failed to create package directories: {str(e)}")


def create_package_files(root_dir, sanitized_name, package_name, author, year, github_username):
    """
    Create all the necessary files for the package.
    
    Args:
        root_dir: Root directory path
        sanitized_name: Sanitized package name
        package_name: Original package name
        author: Author name
        year: License year
        github_username: GitHub username
        
    Raises:
        PackageError: If file creation fails
    """
    try:
        package_dir = root_dir / sanitized_name
        tests_dir = root_dir / "tests"
        
        # Create package module files
        create_package_module_files(package_dir, sanitized_name)
        
        # Create test files
        create_test_files(tests_dir, sanitized_name)
        
        # Create root-level files
        create_root_files(root_dir, sanitized_name, package_name, author, year, github_username)
    except Exception as e:
        raise PackageError(f"Failed to create package files: {str(e)}")


def create_package_module_files(package_dir, sanitized_name):
    """
    Create the Python module files for the package.
    
    Args:
        package_dir: Package directory path
        sanitized_name: Sanitized package name
        
    Raises:
        PackageError: If file creation fails
    """
    try:
        try_operation(
            lambda: create_file(package_dir / "__init__.py", render_template('init_py')),
            f"Failed to create __init__.py",
            PackageError
        )
        
        try_operation(
            lambda: create_file(package_dir / "__main__.py", render_template('main_py')),
            f"Failed to create __main__.py",
            PackageError
        )
    except Exception as e:
        raise PackageError(f"Failed to create module files: {str(e)}")


def create_test_files(tests_dir, sanitized_name):
    """
    Create test files for the package.
    
    Args:
        tests_dir: Tests directory path
        sanitized_name: Sanitized package name
        
    Raises:
        PackageError: If file creation fails
    """
    try:
        try_operation(
            lambda: create_file(tests_dir / f"test_{sanitized_name}.py", render_template('test_py')),
            f"Failed to create test_{sanitized_name}.py",
            PackageError
        )
        
        try_operation(
            lambda: create_file(tests_dir / "run_tests.py", render_template('run_tests_py')),
            f"Failed to create run_tests.py",
            PackageError
        )
    except Exception as e:
        raise PackageError(f"Failed to create test files: {str(e)}")


def create_root_files(root_dir, sanitized_name, package_name, author, year, github_username):
    """
    Create root directory files.
    
    Args:
        root_dir: Root directory path
        sanitized_name: Sanitized package name
        package_name: Original package name
        author: Author name
        year: License year
        github_username: GitHub username
        
    Raises:
        PackageError: If file creation fails
    """
    try:
        create_setup_py(root_dir, sanitized_name, package_name, author, github_username)
        create_readme(root_dir, package_name, sanitized_name)
        create_misc_files(root_dir, year, author)
    except Exception as e:
        raise PackageError(f"Failed to create root files: {str(e)}")


def create_setup_py(root_dir, sanitized_name, package_name, author, github_username):
    """
    Create setup.py file.
    
    Args:
        root_dir: Root directory path
        sanitized_name: Sanitized package name
        package_name: Original package name
        author: Author name
        github_username: GitHub username
        
    Raises:
        PackageError: If file creation fails
    """
    try_operation(
        lambda: create_file(
            root_dir / "setup.py", 
            render_template('setup_py')
        ),
        f"Failed to create setup.py",
        PackageError
    )


def create_readme(root_dir, package_name, sanitized_name):
    """
    Create README.md file.
    
    Args:
        root_dir: Root directory path
        package_name: Original package name
        sanitized_name: Sanitized package name
        
    Raises:
        PackageError: If file creation fails
    """
    try_operation(
        lambda: create_file(
            root_dir / "README.md", 
            render_template('readme')
        ),
        f"Failed to create README.md",
        PackageError
    )


def create_misc_files(root_dir, year, author):
    """
    Create miscellaneous root files.
    
    Args:
        root_dir: Root directory path
        year: License year
        author: Author name
        
    Raises:
        PackageError: If file creation fails
    """
    try:
        try_operation(
            lambda: create_file(root_dir / "MANIFEST.in", render_template('manifest_in')),
            f"Failed to create MANIFEST.in",
            PackageError
        )
        
        try_operation(
            lambda: create_file(root_dir / "pyproject.toml", render_template('pyproject_toml')),
            f"Failed to create pyproject.toml",
            PackageError
        )
        
        try_operation(
            lambda: create_file(root_dir / "LICENSE", render_template('license_mit')),
            f"Failed to create LICENSE",
            PackageError
        )
        
        try_operation(
            lambda: create_file(root_dir / ".gitignore", render_template('gitignore')),
            f"Failed to create .gitignore",
            PackageError
        )
    except Exception as e:
        raise PackageError(f"Failed to create miscellaneous files: {str(e)}")


def print_creation_summary(sanitized_name):
    """
    Print a summary of the created package structure.
    
    Args:
        sanitized_name: Sanitized package name
    """
    print(f"\nPackage successfully created with the following structure:")
    print(f"./")
    print(f"├── {sanitized_name}/")
    print(f"│   ├── __init__.py")
    print(f"│   └── __main__.py")
    print(f"├── tests/")
    print(f"│   ├── test_{sanitized_name}.py")
    print(f"│   └── run_tests.py")
    print(f"├── setup.py")
    print(f"├── README.md")
    print(f"├── MANIFEST.in")
    print(f"├── pyproject.toml")
    print(f"├── LICENSE")
    print(f"└── .gitignore")