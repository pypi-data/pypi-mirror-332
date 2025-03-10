"""
Package creation module for pkgmngr.

This module provides functionality for creating new Python packages with
standard project structure and managing package lifecycle.
"""

from .core import create_package_structure
from .github import init_git_repo, get_github_username_from_git