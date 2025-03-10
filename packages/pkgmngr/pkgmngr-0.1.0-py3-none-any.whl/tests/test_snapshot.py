"""
Tests for the snapshot functionality.
"""
import os
import re
import pytest
from pathlib import Path
from pkgmngr.snapshot.snapshot import (
    create_snapshot,
    parse_snapshot_file,
    get_file_tree,
    should_ignore,
    load_gitignore_patterns
)
from pkgmngr.snapshot.restore import (
    restore_from_snapshot,
    selective_restore
)


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
    assert "# Package Snapshot - Generated on 2025-01-01_12-00-00" in content
    assert "## Comments\nTest snapshot" in content
    assert "## Directory Structure" in content
    assert "## Table of Contents" in content
    assert "## Files" in content


def test_parse_snapshot_file(sample_project, monkeypatch):
    """Test parsing a snapshot file."""
    # Create a snapshot first
    monkeypatch.setattr('time.strftime', lambda *args, **kwargs: "2025-01-01_12-00-00")
    snapshot_file = create_snapshot(sample_project, "snapshots", comment="Test snapshot")
    
    # Parse it
    file_contents, comment = parse_snapshot_file(snapshot_file)
    
    # Verify parsed contents
    assert comment == "Test snapshot"
    assert "test_pkg/__init__.py" in file_contents
    assert "test_pkg/__main__.py" in file_contents
    assert "README.md" in file_contents
    
    # Check content of a specific file
    assert '__version__ = "0.1.0"' in file_contents["test_pkg/__init__.py"]


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
    # Create a regular snapshot file
    regular_snapshot = temp_dir / "regular_snapshot.md"
    regular_snapshot.write_text("# Package Snapshot - Generated on 2025-01-01\n\n## Comments\nRegular snapshot comment\n")
    
    # Create a backup snapshot file (by filename)
    backup_by_name = temp_dir / "pre_restore_backup_2025-01-01.md"
    backup_by_name.write_text("# Package Snapshot - Generated on 2025-01-01\n\n## Comments\nSome comment\n")
    
    # Create a backup snapshot file (by content)
    backup_by_content = temp_dir / "snapshot_with_backup_comment.md"
    backup_by_content.write_text("# Package Snapshot - Generated on 2025-01-01\n\n## Comments\nAutomatic backup created before restoration\n")
    
    # Test detection
    assert not is_backup_snapshot(str(regular_snapshot))
    assert is_backup_snapshot(str(backup_by_name))
    assert is_backup_snapshot(str(backup_by_content))


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
        return file_contents, "Test snapshot"
    
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