"""
Tests for the snapshot functionality.
"""
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import os
import re

from pkgmngr.snapshot.snapshot import (
    create_snapshot,
    parse_snapshot_file,
    get_file_tree,
    extract_project_name_from_snapshot,
    get_package_name_for_snapshot
)
from pkgmngr.snapshot.restore import (
    restore_from_snapshot,
    display_snapshot_metadata,
    create_backup_snapshot
)



def test_get_package_name_for_snapshot(temp_dir, monkeypatch):
    """Test retrieving package name for snapshot."""
    # Test with config file
    config_content = {
        "package_name": "test-config-package"
    }
    
    # Mock the load_config function
    def mock_load_config(path):
        return config_content, "dummy_path"
    
    monkeypatch.setattr("pkgmngr.common.config.load_config", mock_load_config)
    
    # Should get name from config
    name = get_package_name_for_snapshot(temp_dir)
    assert name == "test-config-package"
    
    # Test with failed config loading
    def mock_load_config_fail(path):
        raise Exception("Config not found")
    
    monkeypatch.setattr("pkgmngr.common.config.load_config", mock_load_config_fail)
    
    # Should fall back to directory name
    name = get_package_name_for_snapshot(temp_dir)
    assert name == os.path.basename(temp_dir)

def test_extract_project_name_from_snapshot():
    """Test extracting project name from snapshot header."""
    # New format
    content = "# test-project - Package Snapshot - Generated on 2025-01-01_12-00-00\n\n## Comments"
    name = extract_project_name_from_snapshot(content)
    assert name == "test-project"
    
    # Old format
    content = "# Package Snapshot - Generated on 2025-01-01_12-00-00\n\n## Comments"
    name = extract_project_name_from_snapshot(content)
    assert name is None

@pytest.fixture
def sample_project(temp_dir):
    """Create a sample project structure for snapshot testing."""
    # Create a simple project structure
    pkg_dir = temp_dir / "test_pkg"
    pkg_dir.mkdir()
    
    # Create some Python files
    init_py = pkg_dir / "__init__.py"
    init_py.write_text('"""Test package."""\n\n__version__ = "0.1.0"')
    
    main_py = pkg_dir / "__main__.py"
    main_py.write_text('"""Main module."""\n\nprint("Hello from test_pkg!")')
    
    # Create a README
    readme = temp_dir / "README.md"
    readme.write_text("# Test Package\n\nA test package for snapshot testing.")
    
    # Create a .gitignore file
    gitignore = temp_dir / ".gitignore"
    gitignore.write_text("__pycache__/\n*.py[cod]\n*$py.class\n\n# Snapshots\nsnapshots/")
    
    return temp_dir


def test_create_snapshot(sample_project, monkeypatch):
    """Test creating a snapshot from a project."""
    # Mock time.strftime to return a fixed timestamp
    import time
    monkeypatch.setattr(time, "strftime", lambda *args, **kwargs: "2025-01-01_12-00-00")
    
    # Create snapshot
    output_file = create_snapshot(sample_project, "snapshots", comment="Test snapshot")
    
    # Check that the snapshot file was created
    snapshot_dir = sample_project / "snapshots"
    expected_file = snapshot_dir / "snapshot_2025-01-01_12-00-00.md"
    assert output_file == str(expected_file)
    assert expected_file.exists()
    
    # Check content
    content = expected_file.read_text()
    assert "- Package Snapshot - Generated on 2025-01-01_12-00-00" in content
    assert "## Comments\nTest snapshot" in content
    assert "## Directory Structure" in content
    assert "## Table of Contents" in content
    assert "## Files" in content

def test_create_snapshot_header(sample_project, monkeypatch):
    """Test that create_snapshot includes the project name and note in the header."""
    # Mock time.strftime to return a fixed timestamp
    monkeypatch.setattr('time.strftime', lambda *args, **kwargs: "2025-01-01_12-00-00")
    
    # Mock get_package_name_for_snapshot to return a known value
    monkeypatch.setattr(
        'pkgmngr.snapshot.snapshot.get_package_name_for_snapshot', 
        lambda path: "test-project"
    )
    
    # Create snapshot
    output_file = create_snapshot(sample_project, "snapshots", comment="Test snapshot")
    
    # Check content
    snapshot_path = Path(output_file)
    assert snapshot_path.exists()
    
    with open(snapshot_path, 'r') as f:
        content = f.read()
    
    # Verify the header includes the project name
    assert content.startswith("# test-project - Package Snapshot - Generated on")
    
    # Verify the note about triple primes is included
    assert "**Note:** All triple prime characters (′′′) within file content blocks should be interpreted as triple backticks." in content
    assert "This convention prevents formatting issues in the snapshot markdown." in content

def test_parse_snapshot_file(temp_dir):
    """Test parsing a snapshot file with the new header format."""
    # Create a test snapshot file with new format
    snapshot_file = temp_dir / "test_snapshot.md"
    with open(snapshot_file, "w") as f:
        f.write("""# test-project - Package Snapshot - Generated on 2025-01-01_12-00-00

## Comments
Test snapshot comment

## Directory Structure
```
📦 test_project
├─ 📂 test_pkg
│  ├─ 🐍 __init__.py
│  └─ 🐍 __main__.py
├─ 📝 README.md
└─ 📋 .gitignore
```

## Table of Contents
1. [test_pkg/__init__.py](#test_pkg-__init__py)
2. [test_pkg/__main__.py](#test_pkg-__main__py)
3. [README.md](#readmemd)
4. [.gitignore](#gitignore)

## Files

<a id="test_pkg-__init__py"></a>
### test_pkg/__init__.py
```python
\"\"\"Test package.\"\"\"

__version__ = "0.1.0"
```

<a id="test_pkg-__main__py"></a>
### test_pkg/__main__.py
```python
\"\"\"Main module.\"\"\"

print("Hello from test_pkg!")
```

<a id="readmemd"></a>
### README.md
```markdown
# Test Package

A test package for snapshot testing.
```

<a id="gitignore"></a>
### .gitignore
```
__pycache__/
*.py[cod]
*$py.class

# Snapshots
snapshots/
```
""")
    
    # Test parsing
    file_contents, comment, project_name = parse_snapshot_file(str(snapshot_file))
    
    # Verify results
    assert comment == "Test snapshot comment"
    assert project_name == "test-project"
    assert "test_pkg/__init__.py" in file_contents
    assert "__version__ = \"0.1.0\"" in file_contents["test_pkg/__init__.py"]

def test_create_snapshot_includes_project_name(sample_project, monkeypatch):
    """Test that create_snapshot includes the project name in the header."""
    # Mock time.strftime to return a fixed timestamp
    monkeypatch.setattr('time.strftime', lambda *args, **kwargs: "2025-01-01_12-00-00")
    
    # Mock get_package_name_for_snapshot to return a known value
    monkeypatch.setattr(
        'pkgmngr.snapshot.snapshot.get_package_name_for_snapshot', 
        lambda path: "test-project"
    )
    
    # Create snapshot
    output_file = create_snapshot(sample_project, "snapshots", comment="Test snapshot")
    
    # Check content
    snapshot_path = Path(output_file)
    assert snapshot_path.exists()
    
    with open(snapshot_path, 'r') as f:
        content = f.read()
    
    # Verify the header includes the project name
    assert content.startswith("# test-project - Package Snapshot - Generated on")

def test_display_snapshot_metadata(capsys):
    """Test that the snapshot metadata display function works correctly."""
    # Test with both project name and comment
    display_snapshot_metadata("Test comment", "test-project")
    captured = capsys.readouterr()
    assert "Restoring snapshot of project: test-project" in captured.out
    assert "Test comment" in captured.out
    
    # Test with only comment
    display_snapshot_metadata("Only comment", None)
    captured = capsys.readouterr()
    assert "Restoring snapshot of project" not in captured.out
    assert "Only comment" in captured.out
    
    # Test with only project name
    display_snapshot_metadata(None, "only-project")
    captured = capsys.readouterr()
    assert "Restoring snapshot of project: only-project" in captured.out
    assert "Snapshot comment" not in captured.out
    
    # Test with neither
    display_snapshot_metadata(None, None)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_restore_from_snapshot(sample_project, temp_dir, monkeypatch):
    """Test restoring a project from a snapshot."""
    # Create snapshot of sample project
    monkeypatch.setattr('time.strftime', lambda *args, **kwargs: "2025-01-01_12-00-00")
    snapshot_file = create_snapshot(sample_project, "snapshots", comment="Test snapshot")
    
    # Create a new empty directory to restore to
    restore_dir = temp_dir / "restore_test"
    restore_dir.mkdir()
    
    # Restore from snapshot
    monkeypatch.setattr('builtins.print', lambda *args, **kwargs: None)  # Silence prints
    backup_file = restore_from_snapshot(
        snapshot_file, 
        str(restore_dir), 
        mode='overwrite',
        create_backup=False
    )
    
    # Check that files were restored
    assert (restore_dir / "test_pkg" / "__init__.py").exists()
    assert (restore_dir / "test_pkg" / "__main__.py").exists()
    assert (restore_dir / "README.md").exists()
    
    # Check content of a restored file
    with open(restore_dir / "test_pkg" / "__init__.py", 'r') as f:
        content = f.read()
        assert '__version__ = "0.1.0"' in content

def test_backtick_handling(temp_dir):
    """Test that backticks in file content are properly handled."""
    # Create a test file with triple backticks inside
    test_file = temp_dir / "test_file.md"
    with open(test_file, "w") as f:
        f.write("""# Test File

Here's a code example:

```python
def test_function():
    print("Hello world")
```

And another one:

```javascript
console.log("Hello world");
```
""")
    
    # Create a mock file list
    file_paths = ["test_file.md"]
    
    # Call the collect_file_contents function
    from pkgmngr.snapshot.snapshot import collect_file_contents
    content_lines = collect_file_contents(temp_dir, file_paths)
    
    # Join the lines to check the result
    content = "\n".join(content_lines)
    
    # Verify the backticks were handled correctly
    assert "```markdown" in content  # Outer code block uses regular backticks
    assert "′′′python" in content   # Inner code blocks use primes
    assert "′′′javascript" in content
    
    # Extract the file content
    from pkgmngr.snapshot.snapshot import extract_file_contents_from_snapshot
    file_contents = extract_file_contents_from_snapshot(content)
    
    # Verify extraction works correctly and backticks are restored
    assert "test_file.md" in file_contents
    assert "```python" in file_contents["test_file.md"]  # Primes converted back to backticks
    assert "```javascript" in file_contents["test_file.md"]

@pytest.mark.parametrize("has_project_name", [True, False])
def test_restore_from_snapshot_with_project_name(sample_project, temp_dir, monkeypatch, has_project_name):
    """Test restoring a snapshot with or without project name in the header."""
    # Create a directory to restore to
    restore_dir = temp_dir / "restore_test"
    restore_dir.mkdir()
    
    # Mock parse_snapshot_file to return controlled results
    def mock_parse_snapshot_file(path):
        file_contents = {
            "test_file.py": "print('test')"
        }
        project_name = "test-project" if has_project_name else None
        return file_contents, "Test comment", project_name
    
    monkeypatch.setattr("pkgmngr.snapshot.restore.parse_snapshot_file", mock_parse_snapshot_file)
    
    # Mock other functions to isolate the test
    monkeypatch.setattr("pkgmngr.snapshot.restore.validate_restore_parameters", lambda *args: None)
    monkeypatch.setattr("pkgmngr.snapshot.restore.is_backup_snapshot", lambda path: False)
    monkeypatch.setattr("pkgmngr.snapshot.restore.create_backup_if_needed", lambda *args: None)
    monkeypatch.setattr("pkgmngr.snapshot.restore.restore_files", lambda *args: (1, 0))
    monkeypatch.setattr("pkgmngr.snapshot.restore.print_restore_summary", lambda *args: None)
    
    # Mock display_snapshot_metadata to check it's called with correct args
    display_mock = MagicMock()
    monkeypatch.setattr("pkgmngr.snapshot.restore.display_snapshot_metadata", display_mock)
    
    # Run the restore
    restore_from_snapshot("dummy_path", str(restore_dir))
    
    # Verify display_snapshot_metadata was called with correct arguments
    display_mock.assert_called_once_with("Test comment", "test-project" if has_project_name else None)


def test_selective_restore(sample_project, temp_dir, monkeypatch):
    """Test selectively restoring files from a snapshot."""
    # Create snapshot of sample project
    monkeypatch.setattr('time.strftime', lambda *args, **kwargs: "2025-01-01_12-00-00")
    snapshot_file = create_snapshot(sample_project, "snapshots", comment="Test snapshot")
    
    # Create a new empty directory to restore to
    restore_dir = temp_dir / "selective_restore_test"
    restore_dir.mkdir()
    
    # Selectively restore only Python files
    monkeypatch.setattr('builtins.print', lambda *args, **kwargs: None)  # Silence prints
    backup_file = selective_restore(
        snapshot_file,
        str(restore_dir),
        patterns=["*.py"],  # Only restore Python files
        exclude_patterns=None,
        interactive=False,
        mode='overwrite',
        create_backup=False
    )
    
    # Check that Python files were restored but README was not
    assert (restore_dir / "test_pkg" / "__init__.py").exists()
    assert (restore_dir / "test_pkg" / "__main__.py").exists()
    assert not (restore_dir / "README.md").exists()

"""
Additional tests for the refactored snapshot and restore functionality.
"""
import os
import pytest
from pathlib import Path
from pkgmngr.snapshot.restore import (
    is_backup_snapshot,
    filter_files_by_patterns,
    restore_files,
    selective_restore
)


def test_is_backup_snapshot(temp_dir):
    """Test detecting backup snapshot files."""
    # Create a regular snapshot file with the new format
    regular_snapshot = temp_dir / "regular_snapshot.md"
    regular_snapshot.write_text("# test-project - Package Snapshot - Generated on 2025-01-01\n\n## Comments\nRegular snapshot comment\n")
    
    # Create a backup snapshot file (by filename)
    backup_by_name = temp_dir / "pre_restore_backup_2025-01-01.md"
    backup_by_name.write_text("# test-project - Package Snapshot - Generated on 2025-01-01\n\n## Comments\nSome comment\n")
    
    # Create a backup snapshot file (by content)
    backup_by_content = temp_dir / "snapshot_with_backup_comment.md"
    backup_by_content.write_text("# test-project - Package Snapshot - Generated on 2025-01-01\n\n## Comments\nAutomatic backup created before restoration\n")
    
    # Test detection
    assert not is_backup_snapshot(str(regular_snapshot))
    assert is_backup_snapshot(str(backup_by_name))
    assert is_backup_snapshot(str(backup_by_content))


def test_create_backup_snapshot(temp_dir, monkeypatch):
    """Test creating a backup snapshot."""
    # Mock create_snapshot to return a known path
    snapshot_path = temp_dir / "snapshots" / "snapshot_2025-01-01_12-00-00.md"
    
    def mock_create_snapshot(path, output_folder, output_file, comment):
        os.makedirs(os.path.join(path, output_folder), exist_ok=True)
        with open(snapshot_path, "w") as f:
            f.write(f"# test-project - Package Snapshot - Generated on 2025-01-01_12-00-00\n\n## Comments\n{comment}\n")
        return str(snapshot_path)
    
    monkeypatch.setattr("pkgmngr.snapshot.restore.create_snapshot", mock_create_snapshot)
    monkeypatch.setattr("time.strftime", lambda *args, **kwargs: "2025-01-01_12-00-00")
    
    # Create the backup
    backup_file = create_backup_snapshot(str(temp_dir))
    
    # Check the backup was created with correct naming
    assert "pre_restore_backup_2025-01-01_12-00-00.md" in backup_file
    
    # Verify the content includes the automatic backup comment
    with open(backup_file, "r") as f:
        content = f.read()
    assert "Automatic backup created before restoration" in content
    assert "# test-project - Package Snapshot" in content

# Updated test that correctly expects behavior of dir/* to match all files under dir/
def test_filter_files_by_patterns():
    """Test filtering files by patterns."""
    # Sample file contents
    file_contents = {
        "file1.py": "content1",
        "file2.txt": "content2",
        "dir/file3.py": "content3",
        "dir/file4.txt": "content4",
        "dir/subdir/file5.py": "content5"
    }
    
    # Test with no patterns (should return all files)
    result = filter_files_by_patterns(file_contents)
    assert len(result) == 5
    assert set(result.keys()) == set(file_contents.keys())
    
    # Test with inclusion patterns
    result = filter_files_by_patterns(file_contents, patterns=["*.py"])
    assert len(result) == 3
    assert "file1.py" in result
    assert "dir/file3.py" in result
    assert "dir/subdir/file5.py" in result
    assert "file2.txt" not in result
    
    # Test with directory pattern - matches all files under dir/ including subdirectories
    result = filter_files_by_patterns(file_contents, patterns=["dir/*"])
    assert len(result) == 3
    assert "dir/file3.py" in result
    assert "dir/file4.txt" in result
    assert "dir/subdir/file5.py" in result
    
    # Test with direct children pattern - use a more specific pattern to match only direct children
    result = filter_files_by_patterns(file_contents, patterns=["dir/file*"])
    assert len(result) == 2
    assert "dir/file3.py" in result
    assert "dir/file4.txt" in result
    assert "dir/subdir/file5.py" not in result


def test_restore_files(temp_dir):
    """Test restoring files with different modes."""
    # Sample file contents
    file_contents = {
        "file1.py": "content1",
        "dir/file2.py": "content2",
        "binary.bin": "[Binary file - contents not shown]"
    }
    
    # Create the directory structure
    (temp_dir / "dir").mkdir(exist_ok=True)
    
    # Test with overwrite mode (default)
    files_restored, files_skipped = restore_files(file_contents, temp_dir)
    assert files_restored == 2  # Binary file should be skipped
    assert files_skipped == 1
    
    # Check that files were created
    assert (temp_dir / "file1.py").exists()
    assert (temp_dir / "dir" / "file2.py").exists()
    assert not (temp_dir / "binary.bin").exists()
    
    # Modify a file to test overwrites
    (temp_dir / "file1.py").write_text("modified content")
    
    # Test with safe mode
    files_restored, files_skipped = restore_files(
        {"file1.py": "new content", "new_file.py": "new file content"},
        temp_dir,
        mode="safe"
    )
    assert files_restored == 1  # Only new_file.py should be restored
    assert files_skipped == 1   # file1.py should be skipped
    
    # Check that existing file wasn't overwritten
    assert (temp_dir / "file1.py").read_text() == "modified content"
    assert (temp_dir / "new_file.py").exists()
    
    # Test with overwrite mode
    files_restored, files_skipped = restore_files(
        {"file1.py": "overwritten content"},
        temp_dir,
        mode="overwrite"
    )
    assert files_restored == 1
    assert files_skipped == 0
    
    # Check that file was overwritten
    assert (temp_dir / "file1.py").read_text() == "overwritten content"


def test_selective_restore(temp_dir, monkeypatch):
    """Test selective restoration with patterns."""
    # Create a snapshot file
    snapshot_file = temp_dir / "test_snapshot.md"

    # Create the actual file to prevent file not found error
    snapshot_file.write_text("# Test Snapshot")
    
    # Mock parse_snapshot_file to return a predefined set of files
    def mock_parse_snapshot_file(path):
        file_contents = {
            "file1.py": "content1",
            "file2.txt": "content2",
            "dir/file3.py": "content3",
            "dir/file4.txt": "content4"
        }
        return file_contents, "Test snapshot", "test-project"
    
    monkeypatch.setattr(
        "pkgmngr.snapshot.restore.parse_snapshot_file", 
        mock_parse_snapshot_file
    )
    
    # Mock other functions to avoid creating actual backups
    monkeypatch.setattr(
        "pkgmngr.snapshot.restore.is_backup_snapshot",
        lambda path: False
    )
    monkeypatch.setattr(
        "pkgmngr.snapshot.restore.create_backup_snapshot",
        lambda *args, **kwargs: str(temp_dir / "mock_backup.md")
    )
    
    # Test restoring with patterns
    target_dir = temp_dir / "restore_target"
    target_dir.mkdir()
    
    result = selective_restore(
        str(snapshot_file),
        str(target_dir),
        patterns=["*.py"],
        create_backup=True
    )
    
    # Check that only Python files were restored
    assert (target_dir / "file1.py").exists()
    assert (target_dir / "dir" / "file3.py").exists()
    assert not (target_dir / "file2.txt").exists()
    assert not (target_dir / "dir" / "file4.txt").exists()
    
    # Test with interactive selection - mock the interactive function
    def mock_select_interactive(files, target):
        # Simulate user selecting only file2.txt
        return {"file2.txt": "content2"}
    
    monkeypatch.setattr(
        "pkgmngr.snapshot.restore.select_files_interactive",
        mock_select_interactive
    )
    
    # Clear the target directory
    import shutil
    shutil.rmtree(target_dir)
    target_dir.mkdir()
    
    # Test with interactive selection
    result = selective_restore(
        str(snapshot_file),
        str(target_dir),
        interactive=True,
        create_backup=False
    )
    
    # Check that only the interactively selected file was restored
    assert not (target_dir / "file1.py").exists()
    assert (target_dir / "file2.txt").exists()