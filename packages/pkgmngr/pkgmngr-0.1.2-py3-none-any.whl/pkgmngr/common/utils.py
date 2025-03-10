"""
Common utility functions used across pkgmngr modules.
"""
import os
import re
from pathlib import Path


def create_directory(path):
    """
    Create a directory if it doesn't exist.
    
    Args:
        path: Path to the directory
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")


def create_file(path, content):
    """
    Create a file with the given content.
    
    Args:
        path: Path to the file
        content: Content of the file
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {path}")


def sanitize_package_name(name):
    """
    Sanitize package name to be a valid Python package name.
    
    Args:
        name: Package name to sanitize
    
    Returns:
        str: Sanitized package name
    """
    # Replace dashes with underscores for Python compatibility
    return name.replace('-', '_')


def is_binary_file(file_path):
    """
    Determine if a file is binary by checking its content.
    
    Args:
        file_path: Path to the file to check
        
    Returns:
        True if the file appears to be binary, False otherwise
    """
    try:
        # Try to open the file in text mode
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read first chunk of the file (4KB is usually enough to determine)
            chunk = f.read(4096)
            
            # Check for common binary file signatures
            # This approach looks for null bytes and other control characters
            # that are uncommon in text files
            binary_chars = [
                char for char in chunk 
                if ord(char) < 9 or (ord(char) > 13 and ord(char) < 32)
            ]
            
            # If we found binary characters, it's likely a binary file
            # Use a threshold to avoid false positives with some text files
            if len(binary_chars) > 0:
                return True
                
            return False
    except UnicodeDecodeError:
        # If we can't decode it as UTF-8, it's a binary file
        return True
    except Exception:
        # For any other error, assume it's binary to be safe
        return True