# pkgmngr

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

A comprehensive command line utility that streamlines creation, snapshotting, and lifecycle management of Python packages. Designed for modern Python development workflows, pkgmngr helps developers save time on repetitive setup tasks and enhances collaboration, including AI-assisted development.

## Why pkgmngr?

- **Save Time**: Automate repetitive package setup and maintenance tasks
- **Standardize Structure**: Ensure consistent package layout across projects
- **Simplify Collaboration**: Easily share code context with snapshots
- **Streamline Workflow**: Integrate with GitHub and PyPI in a few commands
- **Enhance AI Collaboration**: Create perfect context snapshots for AI assistants

## Features

### Package Creation
- **Zero Config Setup**: Create standard Python package structures with a single command
- **Templated Files**: Generate all necessary project files (setup.py, README.md, LICENSE, etc.)
- **Git Ready**: Initialize Git repositories with GitHub integration

### Package Snapshots
- **Code Documentation**: Create beautiful markdown snapshots of your entire codebase
- **AI Collaboration**: Perfect for sharing code context with AI assistants
- **Point-in-Time Recovery**: Restore from snapshots with precision control
- **Selective Restoration**: Choose specific files or patterns to restore

### Lifecycle Management
- **Package Evolution**: Rename packages and automatically update all references
- **GitHub Integration**: Push changes to GitHub with a single command
- **PyPI Publishing**: Publish packages to PyPI (or TestPyPI) with ease

## Installation

```bash
# Install from PyPI
pip install pkgmngr

# Or install from source
git clone https://github.com/B4PT0R/pkgmngr.git
cd pkgmngr
pip install -e .
```

## Quick Start

```bash
# Create a new package
pkgmngr new my-package
cd my-package

# Generate the package files
pkgmngr create

# Initialize Git and GitHub repositories (requires GITHUB_TOKEN)
pkgmngr init-repo

# Make some changes to your code...

# Take a snapshot of your project
pkgmngr snapshot -m "Initial implementation"

# Push changes to GitHub
pkgmngr push

# Publish to PyPI when ready
pkgmngr publish
```

## Detailed Usage Guide

### Creating a New Package

The `new` command creates a directory with a configuration file:

```bash
# Create a new package directory with config file
pkgmngr new my-package
```

Output:
```
✅ Created package directory and config file for 'my-package':
- my-package/pkgmngr.toml

To finish creating your package:
- Change to the project's directory: `cd my-package`
- Review and edit the config file in your favorite editor: e.g. `nano pkgmngr.toml`
- Then run `pkgmngr create` to generate the project files.
...
```

This creates a directory with a `pkgmngr.toml` configuration file. You can edit this file to customize package details before generating the actual structure.

```bash
# Navigate to the new directory
cd my-package

# Review and edit the config file (pkgmngr.toml)
# Then generate the package files
pkgmngr create
```

Output:
```
ℹ️ Creating package structure for 'my-package'...
Created directory: my_package
Created: my_package/__init__.py
Created: my_package/__main__.py
Created directory: tests
Created: tests/test_my_package.py
Created: tests/run_tests.py
Created: setup.py
Created: README.md
Created: MANIFEST.in
Created: pyproject.toml
Created: LICENSE
Created: .gitignore

Package successfully created with the following structure:
./
├── my_package/
│   ├── __init__.py
│   └── __main__.py
├── tests/
│   ├── test_my_package.py
│   └── run_tests.py
├── setup.py
├── README.md
├── MANIFEST.in
├── pyproject.toml
├── LICENSE
└── .gitignore

✅ Package created successfully!
```

The `create` command generates a standard Python package structure based on your configuration.

### Taking Snapshots

Snapshots create comprehensive Markdown documentation of your codebase:

```bash
# Create a snapshot with a comment
pkgmngr snapshot -m "Implemented core features"

# List all available snapshots
pkgmngr snapshot -l
```

Output:
```
Available snapshots:
----------------------------------------------------------------------------------------------------
#   Type     Date                Filename                       Comment
----------------------------------------------------------------------------------------------------
1   SNAPSHOT 2025-03-10 15:30:45 snapshot_2025-03-10_15-30-45.md Implemented core features
----------------------------------------------------------------------------------------------------
```

Snapshots include:
- Directory structure with file type icons
- Navigable table of contents
- All file contents with proper syntax highlighting
- Metadata and comments

### Restoring from Snapshots

```bash
# Restore from a specific snapshot (by number)
pkgmngr restore 1

# Interactively select files to restore
pkgmngr restore -i

# Restore only Python files
pkgmngr restore -p "*.py"

# Exclude certain files
pkgmngr restore -e "temp_*.py"

# Specify restore mode (safe, overwrite, force)
pkgmngr restore 1 -m safe
```

Restoration modes:
- `safe`: Skips existing files
- `overwrite`: Replaces existing files (default)
- `force`: Replaces all files, including read-only

### Package Lifecycle Management

#### Renaming Packages

Renaming packages is often a pain in the neck...
The `rename` command allows you to change your package name and automatically updates all references to that name across your package with ease:

```bash
# Rename a package (and update all references)
pkgmngr rename old-package-name new-package-name
```

This command:
- Updates the package directory name (`old_name` → `new_name`)
- Updates all occurences of the old name found across directory names, file names, and file contents of your whole project.
- Renames the online GitHub repository too (if any).

Output:
```
ℹ️ Updated config file with new package name: new-package-name
ℹ️ Renamed package directory: old_package_name → new_package_name
ℹ️ Updated references in README.md
...
✅ Project successfully renamed from 'old-package-name' to 'new-package-name'
```

Example usage:
```bash
# Before: my-package (directory: my_package)
pkgmngr rename my-package awesome-package
# After: awesome-package (directory: awesome_package)
```

Note that this command must be run from the package root directory (where the `pkgmngr.toml` file is located).

#### GitHub Integration

##### GitHub Personal Access Token

For GitHub integration, you'll need a GitHub Personal Access Token with the `repo` scope:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with the `repo` scope
3. Set it as the `GITHUB_TOKEN` environment variable:
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

##### Usage

Initialize Git and create a GitHub repository:

```bash
# Initialize Git and GitHub repositories
pkgmngr init-repo
```

Output:
```
ℹ️ Detected GitHub repository: yourusername/my-package
ℹ️ Initialized empty Git repository
ℹ️ Created initial commit
ℹ️ Creating GitHub repository: yourusername/my-package...
✅ Created GitHub repository: yourusername/my-package
ℹ️ Pushing code to GitHub...
✅ Pushed code to GitHub: https://github.com/yourusername/my-package.git
✅ Repository initialization completed successfully!
```

Then you can push the changes you make to your code using the `push` command

```bash
# Push changes to GitHub (with interactive commit message)
pkgmngr push
```

#### PyPI Management

##### PyPI/TestPyPI Authentication

Publishing to PyPI or TestPyPI requires properly configured authentication for `twine`. Before using the `publish` command, ensure you have:

1. A PyPI account (and TestPyPI account if using `--test`)
2. Configured `twine` authentication using one of these methods:
   - A `.pypirc` file in your home directory:
     ```ini
     [distutils]
     index-servers=
         pypi
         testpypi

     [pypi]
     username = your_username
     password = your_password

     [testpypi]
     repository = https://test.pypi.org/legacy/
     username = your_testpypi_username
     password = your_testpypi_password
     ```
   - Environment variables: `TWINE_USERNAME` and `TWINE_PASSWORD`
   - Interactive prompt: If credentials aren't found, `twine` will prompt for them

For security, using API tokens instead of passwords is recommended:
1. Generate tokens at https://pypi.org/manage/account/#api-tokens (or https://test.pypi.org/manage/account/#api-tokens)
2. Use the token as your password with username `__token__`

The `pkgmngr publish` command relies on these authentication methods for successful uploads.

##### Usage

```bash
# Publish to TestPyPI
pkgmngr publish --test

# Publish to PyPI with automatic patch version increment
pkgmngr publish
```

The `publish` command allows automatic version increments following semantic versioning principles:

```bash
# Publish to PyPI with automatic patch version increment (e.g., 0.1.0 → 0.1.1)
pkgmngr publish

# Publish to PyPI with a minor version increment (e.g., 0.1.1 → 0.2.0)
pkgmngr publish --bump minor

# Publish to PyPI with a major version increment (e.g., 0.2.0 → 1.0.0)
pkgmngr publish --bump major

# Publish to TestPyPI with version increment
pkgmngr publish --test --bump patch
```

Version information is tracked in your `pkgmngr.toml` configuration file and automatically updated in:
- `pkgmngr.toml` (master record)
- `yourpackage/__init__.py` (`__version__` attribute)
- `setup.py` (package version)

This ensures your package version is consistently maintained across all relevant files when publishing.

## Configuration

The `pkgmngr.toml` file contains configuration settings for your package:

```toml
package_name = "my-package"
version = "0.1.0"
author = "Your Name"
year = "2025"
description = "A Python package named my-package"

[github]
username = "your-username"
private = false

[python]
requires = ">=3.6"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[dependencies]
requires = []
dev_requires = [
    "pytest",
    "pytest-cov",
    "flake8",
    "black",
]
```

## Snapshot Features

### Beautiful Directory Tree

Snapshots include a visually enhanced directory tree with file type icons and proper hierarchy:

```
📦 my_project
├─ 📂 src
│  ├─ 🐍 __init__.py
│  ├─ 🐍 main.py
│  └─ 🐍 utils.py
├─ 📂 tests
│  ├─ 🐍 test_main.py
│  └─ 🐍 test_utils.py
├─ 📝 README.md
└─ 📋 requirements.txt
```

### Navigable Table of Contents

Each snapshot includes a clickable table of contents that links directly to file sections for easy navigation.

### Syntax Highlighting

Code sections are properly syntax-highlighted based on file extensions, making your snapshots readable and beautiful.

## Advanced Usage

### Custom Snapshot Paths

```bash
# Specify a different start path and output folder
pkgmngr snapshot /path/to/project -o custom_snapshots
```

### Gitignore Integration

Snapshots respect your `.gitignore` patterns, but also support special `#pkgmngr` prefixed patterns that only apply to snapshots:

```
# Regular .gitignore pattern (ignored by Git and snapshots)
__pycache__/

# Snapshot-specific pattern (ignored by snapshots only)
#pkgmngr secrets.json
```

### Automatic Backups

When restoring, a backup snapshot is automatically created:

```bash
# Restore without creating a backup
pkgmngr restore 1 --no-backup

# Specify a custom backup location
pkgmngr restore 1 -b /path/to/backup.md
```

## Troubleshooting

### Common Issues

1. **'pkgmngr' command not found**
   - Ensure the installation directory is in your PATH
   - Try installing with `pip install --user pkgmngr`

2. **GitHub authentication errors**
   - Check that your GITHUB_TOKEN environment variable is set correctly
   - Ensure your token has the 'repo' scope

3. **Snapshot restore fails**
   - Check if you have write permissions to all affected files
   - Try using the `-m force` option for stubborn files

### Getting Help

If you encounter any issues not covered here, please file an issue on GitHub: https://github.com/B4PT0R/pkgmngr/issues

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/B4PT0R/pkgmngr.git
cd pkgmngr

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .[dev]
```

### Running Tests

```bash
pytest
# Or with coverage
pytest --cov=pkgmngr tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure your code follows the existing style and passes all tests.

## License

MIT