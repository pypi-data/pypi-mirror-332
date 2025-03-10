"""
Pytest configuration and shared fixtures for pkgmngr tests.
"""
import os
import shutil
import tempfile
import pytest
from pathlib import Path
import sys
import json
from unittest.mock import MagicMock, patch
import io


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


@pytest.fixture
def temp_cwd(temp_dir):
    """Change to a temporary directory during the test."""
    old_cwd = os.getcwd()
    os.chdir(temp_dir)
    yield temp_dir
    os.chdir(old_cwd)


@pytest.fixture
def dummy_package_config():
    """Return a dummy package configuration for testing."""
    return {
        "package_name": "test-pkg",
        "author": "Test Author",
        "year": "2025",
        "description": "A test package",
        "github": {
            "username": "testuser",
            "private": False
        },
        "python": {
            "requires": ">=3.6",
            "classifiers": [
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ]
        },
        "dependencies": {
            "requires": [],
            "dev_requires": [
                "pytest",
                "pytest-cov",
            ]
        }
    }


@pytest.fixture
def mock_toml_file(temp_dir, dummy_package_config):
    """Create a mock pkgmngr.toml file with test configuration."""
    import toml
    config_path = temp_dir / "pkgmngr.toml"
    with open(config_path, "w") as f:
        toml.dump(dummy_package_config, f)
    return config_path


@pytest.fixture
def mock_git_repo(temp_dir, monkeypatch):
    """
    Mock a git repository for testing.
    
    This fixture:
    1. Creates a temporary directory
    2. Monkeypatches subprocess.run to simulate git operations
    3. Returns the temp directory path
    """
    # Create a fake .git directory to simulate a git repo
    git_dir = temp_dir / ".git"
    git_dir.mkdir(exist_ok=True)
    
    # Monkeypatch subprocess.run for git commands
    def mock_run(*args, **kwargs):
        class CompletedProcess:
            def __init__(self, returncode=0, stdout=b"", stderr=b""):
                self.returncode = returncode
                self.stdout = stdout
                self.stderr = stderr
                
        cmd = args[0][0] if args and isinstance(args[0], list) else None
        
        if cmd == "git":
            # Handle different git commands
            subcmd = args[0][1] if len(args[0]) > 1 else ""
            
            if subcmd == "rev-parse":
                return CompletedProcess(returncode=0, stdout=b"true")
            elif subcmd == "remote":
                if "get-url" in args[0]:
                    return CompletedProcess(returncode=0, stdout=b"https://github.com/testuser/test-pkg.git")
            elif subcmd == "status":
                return CompletedProcess(returncode=0, stdout=b" M file1.py\n?? file2.py")
            elif subcmd == "branch":
                return CompletedProcess(returncode=0, stdout=b"main")
            
        # Default response for any other command
        return CompletedProcess()
    
    import subprocess
    monkeypatch.setattr(subprocess, "run", mock_run)
    monkeypatch.setattr(subprocess, "check_output", lambda *args, **kwargs: b"output")
    
    return temp_dir


@pytest.fixture
def mock_github_api(monkeypatch):
    """Mock GitHub API responses."""
    def mock_requests_post(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data
                
            def json(self):
                return self.json_data
                
        # Mock GitHub API responses
        if "api.github.com/user/repos" in args[0]:
            return MockResponse(201, {
                "name": "test-pkg",
                "full_name": "testuser/test-pkg",
                "html_url": "https://github.com/testuser/test-pkg"
            })
        elif "api.github.com/repos" in args[0]:
            return MockResponse(200, {"name": "test-pkg"})
            
        return MockResponse(404, {"message": "Not found"})
        
    import requests
    monkeypatch.setattr(requests, "post", mock_requests_post)
    monkeypatch.setattr(requests, "patch", mock_requests_post)
    
    return None


@pytest.fixture
def capture_stdout():
    """Capture stdout for testing print statements."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    yield captured_output
    sys.stdout = sys.__stdout__


@pytest.fixture
def sample_snapshot_file(temp_dir):
    """Create a sample snapshot markdown file."""
    snapshot_dir = temp_dir / "snapshots"
    snapshot_dir.mkdir(exist_ok=True)
    
    snapshot_file = snapshot_dir / "snapshot_2025-01-01_12-00-00.md"
    with open(snapshot_file, "w") as f:
        f.write("""# Package Snapshot - Generated on 2025-01-01_12-00-00

## Comments
Test snapshot comment

## Directory Structure
′′′
📦 test_project
├─ 📂 test_pkg
│  ├─ 🐍 __init__.py
│  └─ 🐍 __main__.py
├─ 📝 README.md
└─ 📋 .gitignore
′′′

## Table of Contents
1. [test_pkg/__init__.py](#test_pkg-__init__py)
2. [test_pkg/__main__.py](#test_pkg-__main__py)
3. [README.md](#readmemd)
4. [.gitignore](#gitignore)

## Files

<a id="test_pkg-__init__py"></a>
### test_pkg/__init__.py
′′′python
\"\"\"Test package.\"\"\"

__version__ = "0.1.0"
′′′

<a id="test_pkg-__main__py"></a>
### test_pkg/__main__.py
′′′python
\"\"\"Main module.\"\"\"

print("Hello from test_pkg!")
′′′

<a id="readmemd"></a>
### README.md
′′′markdown
# Test Package

A test package for snapshot testing.
′′′

<a id="gitignore"></a>
### .gitignore
′′′
__pycache__/
*.py[cod]
*$py.class

# Snapshots
snapshots/
′′′
""")
    
    return snapshot_file


@pytest.fixture
def mock_py_pkg_structure(temp_dir):
    """Create a minimal Python package structure for testing."""
    pkg_dir = temp_dir / "test_pkg"
    pkg_dir.mkdir(exist_ok=True)
    
    # Create basic package files
    init_file = pkg_dir / "__init__.py"
    init_file.write_text('"""Test package."""\n\n__version__ = "0.1.0"')
    
    main_file = pkg_dir / "__main__.py"
    main_file.write_text('"""Main module."""\n\nprint("Hello from test_pkg!")')
    
    # Create README
    readme = temp_dir / "README.md"
    readme.write_text("# Test Package\n\nA test package for snapshot testing.")
    
    # Create setup.py
    setup_py = temp_dir / "setup.py"
    setup_py.write_text('''from setuptools import setup, find_packages

setup(
    name="test-pkg",
    version="0.1.0",
    packages=["test_pkg"],
    author="Test Author",
    description="A test package",
)
''')
    
    return temp_dir