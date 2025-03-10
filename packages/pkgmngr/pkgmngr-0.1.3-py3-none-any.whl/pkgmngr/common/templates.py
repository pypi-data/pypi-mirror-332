"""
Shared templates used across pkgmngr modules.
"""
import os

def _load_template(template_name):
    """
    Load template content from a file.
    
    Args:
        template_name: Name of the template file without extension
        
    Returns:
        str: Template content
    """
    try:
        # For Python 3.9+: Using importlib.resources.files
        from importlib.resources import files
        template_path = files('pkgmngr.templates').joinpath(f"{template_name}.txt")
        return template_path.read_text(encoding='utf-8')
    except (ImportError, AttributeError):
        # Fallback for older Python versions
        package_dir = os.path.dirname(os.path.dirname(__file__))
        template_path = os.path.join(package_dir, "templates", f"{template_name}.txt")
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()

def get_gitignore_content():
    """Get the default gitignore content."""
    return _load_template("gitignore")

# Functions to load specific templates
def get_license_mit_template():
    """Get the MIT license template."""
    return _load_template("license_mit")

def get_readme_template():
    """Get the README template."""
    return _load_template("readme")

def get_setup_py_template():
    """Get the setup.py template."""
    return _load_template("setup_py")

def get_pyproject_toml_template():
    """Get the pyproject.toml template."""
    return _load_template("pyproject_toml")

def get_manifest_in_template():
    """Get the MANIFEST.in template."""
    return _load_template("manifest_in")

def get_init_py_template():
    """Get the __init__.py template."""
    return _load_template("init_py")

def get_main_py_template():
    """Get the __main__.py template."""
    return _load_template("main_py")

def get_test_py_template():
    """Get the test file template."""
    return _load_template("test_py")

def get_run_tests_py_template():
    """Get the run_tests.py template."""
    return _load_template("run_tests_py")

# For backward compatibility, maintain these constants
GITIGNORE_TEMPLATE = _load_template('gitignore')
LICENSE_MIT = _load_template('license_mit')
README_TEMPLATE = _load_template('readme')
SETUP_PY_TEMPLATE = _load_template('setup_py')
PYPROJECT_TOML_TEMPLATE = _load_template('pyproject_toml')
MANIFEST_IN_TEMPLATE = _load_template('manifest_in')
INIT_PY_TEMPLATE = _load_template('init_py')
MAIN_PY_TEMPLATE = _load_template('main_py')
TEST_PY_TEMPLATE = _load_template('test_py')
RUN_TESTS_PY_TEMPLATE = _load_template('run_tests_py')