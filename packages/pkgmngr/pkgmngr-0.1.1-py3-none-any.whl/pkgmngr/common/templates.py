"""
Shared templates used across pkgmngr modules.
"""

# Default gitignore template shared between snapshot and create modules
DEFAULT_GITIGNORE_TEMPLATE = [
    "# Default .gitignore created by pkgmngr",
    "# Includes common patterns for Python projects",
    "",
    "# pkgmngr config file",
    "pkgmngr.toml",
    "",
    "# pkgmngr snapshots",
    "snapshots/",
    "",
    "# Example of pkgmngr-specific exclusions",
    "# Git will ignore lines with a leading #pkgmngr comment, but snapshot will use them",
    "#pkgmngr my_secret_config.ini",
    "#pkgmngr temporary_work/",
    "",
    "# Python",
    "__pycache__/",
    "*.py[cod]",
    "*$py.class",
    "*.so",
    ".Python",
    "build/",
    "develop-eggs/",
    "dist/",
    "downloads/",
    "eggs/",
    ".eggs/",
    "lib/",
    "lib64/",
    "parts/",
    "sdist/",
    "var/",
    "wheels/",
    "*.egg-info/",
    ".installed.cfg",
    "*.egg",
    ".pytest_cache/",
    ".benchmarks/"
    ".coverage",
    "htmlcov/",
    "",
    "# Virtual environments",
    "venv/",
    ".venv/",
    "env/",
    ".env/",
    "ENV/",
    "",
    "# IDEs and editors",
    ".idea/",
    ".vscode/",
    "*.swp",
    "*.swo",
    ".DS_Store",
    "Thumbs.db",
    "",
    "# Build and distribution",
    "dist/",
    "build/",
    "",
    "# Version control",
    ".git/",
    ".hg/",
    ".svn/",
    ".bzr/",
    "",
    "# Frontend specific",
    "node_modules/",
    "bower_components/",
    "package-lock.json",
    "yarn.lock",
    "npm-debug.log",
    "yarn-error.log",
    "",
    "# Data and logs",
    "logs/",
    "*.log",
    "*.csv",
    "*.sqlite",
    "*.db"
]

def get_gitignore_content():
    """
    Get the default gitignore content as a single string.
    
    Returns:
        str: Default gitignore content
    """
    return '\n'.join(DEFAULT_GITIGNORE_TEMPLATE)

GITIGNORE_TEMPLATE=get_gitignore_content()

# License template
LICENSE_MIT = """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# README template
README_TEMPLATE = """# {package_name}

Brief description of the package.

## Installation

```bash
pip install {package_name}
```

## Usage

```python
import {sanitized_name}

# Example usage
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/username/{package_name}.git
cd {package_name}

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install development dependencies
pip install -e .[dev]
```

### Running Tests

```bash
pytest
```

## License

MIT
"""

# setup.py template
SETUP_PY_TEMPLATE = """from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="{package_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={{
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'black',
        ],
    }},
    author="{author}",
    author_email="your.email@example.com",
    description="A short description of the package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{github_username}/{package_name}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={{
        'console_scripts': [
            '{package_name}={sanitized_name}.__main__:main',
        ],
    }},
)
"""

# pyproject.toml template
PYPROJECT_TOML_TEMPLATE = r"""[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py36', 'py37', 'py38', 'py39']
include = '\.pyi?$'

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
"""

# MANIFEST.in template
MANIFEST_IN_TEMPLATE = """include LICENSE
include README.md
recursive-include tests *
"""

# __init__.py template
INIT_PY_TEMPLATE = """\"\"\"
{package_name} package.
\"\"\"

__version__ = "0.1.0"
"""

# __main__.py template
MAIN_PY_TEMPLATE = """\"\"\"
Main module for {package_name}.
\"\"\"

def main():
    \"\"\"
    Main entry point for the application.
    \"\"\"
    print("Hello from {package_name}!")


if __name__ == "__main__":
    main()
"""

# Test template
TEST_PY_TEMPLATE = """\"\"\"
Test module for {package_name}.
\"\"\"
import pytest
from {package_name} import __version__


def test_version():
    \"\"\"Test version is a string.\"\"\"
    assert isinstance(__version__, str)


def test_hello():
    \"\"\"Test a simple function.\"\"\"
    # Replace with actual tests for your package
    assert True
"""

# Run tests template
RUN_TESTS_PY_TEMPLATE = """\"\"\"
Script to run all tests for {package_name}.
\"\"\"
import pytest
import sys
import os
import argparse
import coverage


def run_tests_with_coverage(verbose=False, html_report=False):
    \"\"\"Run tests with coverage measurement.\"\"\"
    # Start coverage measurement
    cov = coverage.Coverage(
        source=['{package_name}'],
        omit=['*/tests/*', '*/site-packages/*']
    )
    cov.start()

    # Discover and run tests
    verbosity = 2 if verbose else 1
    exit_code = pytest.main(['--verbose'] if verbose else [])
    
    # Stop coverage measurement
    cov.stop()
    cov.save()
    
    # Report coverage
    print("\\nCoverage Summary:")
    cov.report()
    
    # Generate HTML report if requested
    if html_report:
        html_dir = os.path.join('tests', 'htmlcov')
        cov.html_report(directory=html_dir)
        print(f"\\nHTML coverage report generated in {{html_dir}}")
    
    return exit_code


def run_tests(verbose=False):
    \"\"\"Run tests without coverage measurement.\"\"\"
    verbosity = 2 if verbose else 1
    return pytest.main(['--verbose'] if verbose else [])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run tests for {package_name}')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-c', '--coverage', action='store_true', help='Run with coverage measurement')
    parser.add_argument('--html', action='store_true', help='Generate HTML coverage report')
    
    args = parser.parse_args()
    
    if args.coverage:
        try:
            exit_code = run_tests_with_coverage(args.verbose, args.html)
        except ImportError:
            print("Error: The 'coverage' package is required to run tests with coverage.")
            print("Install it with: pip install coverage")
            exit_code = 1
    else:
        exit_code = run_tests(args.verbose)
    
    sys.exit(exit_code)
"""