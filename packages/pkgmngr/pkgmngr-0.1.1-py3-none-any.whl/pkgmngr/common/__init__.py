"""
Common utilities module for pkgmngr.

This module provides shared functionality used by different components
of the pkgmngr package.
"""

from .utils import create_directory, sanitize_package_name
from .templates import get_gitignore_content
from .pypi import check_name_availability, is_name_available_on_pypi