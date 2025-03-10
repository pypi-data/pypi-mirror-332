"""
Functionality to restore directory structures from snapshot files.
"""
import os
import re
import time
import fnmatch
from typing import Optional, Dict, Tuple, List, Set
from pathlib import Path

from pkgmngr.common.utils import create_file, create_directory
from pkgmngr.common.errors import RestoreError, try_operation, assert_condition
from .snapshot import create_snapshot, parse_snapshot_file


def restore_from_snapshot(snapshot_file_path: str, target_dir: str, 
                          mode: str = 'overwrite', create_backup: bool = True,
                          backup_path: str = None) -> Optional[str]:
    """
    Restore a project structure from a snapshot file.
    
    Args:
        snapshot_file_path: Path to the snapshot file
        target_dir: Directory to restore to
        mode: Restoration mode:
              - 'safe': skips existing files
              - 'overwrite': replaces existing files (default)
              - 'force': replaces all files
        create_backup: Whether to create a backup before restoring
        backup_path: Custom path for the backup file
        
    Returns:
        Path to the backup file if created, None otherwise
        
    Raises:
        RestoreError: If restoration fails
    """
    try:
        validate_restore_parameters(snapshot_file_path, target_dir, mode)
        
        # Ensure target directory exists
        os.makedirs(target_dir, exist_ok=True)
        
        # Check if we're restoring from a backup file
        is_backup = is_backup_snapshot(snapshot_file_path)
        
        # Create backup if requested and needed
        backup_file = create_backup_if_needed(target_dir, create_backup, is_backup, backup_path)
        
        # Parse the snapshot file
        file_contents, comment = parse_snapshot_file(snapshot_file_path)
        
        # Display snapshot comment if present
        display_snapshot_comment(comment)
        
        # Restore files
        print(f"Restoring files to {target_dir}...")
        files_restored, files_skipped = restore_files(file_contents, target_dir, mode)
        
        # Print summary
        print_restore_summary(files_restored, files_skipped, backup_file)
        
        return backup_file
        
    except Exception as e:
        if isinstance(e, RestoreError):
            raise e
        else:
            raise RestoreError(f"Failed to restore from snapshot: {str(e)}")


def validate_restore_parameters(snapshot_file_path, target_dir, mode):
    """
    Validate parameters for restore operation.
    
    Args:
        snapshot_file_path: Path to the snapshot file
        target_dir: Directory to restore to
        mode: Restoration mode
        
    Raises:
        RestoreError: If parameters are invalid
    """
    if not os.path.exists(snapshot_file_path):
        raise RestoreError(f"Snapshot file not found: {snapshot_file_path}")
    
    if mode not in ['safe', 'overwrite', 'force']:
        raise RestoreError(f"Invalid restoration mode: {mode}")


def is_backup_snapshot(snapshot_file_path: str) -> bool:
    """
    Determine if a snapshot file is already a backup file.
    
    Args:
        snapshot_file_path: Path to the snapshot file
        
    Returns:
        True if the file appears to be a backup snapshot, False otherwise
    """
    # Check the filename pattern
    filename = os.path.basename(snapshot_file_path)
    if filename.startswith("pre_restore_backup_"):
        return True
        
    # Check file content for automatic backup comment
    try:
        with open(snapshot_file_path, 'r', encoding='utf-8') as f:
            # Read first 2000 characters which should include the header and comment
            header = f.read(2000)
            
            # Look for the automatic backup comment
            if "## Comments" in header and "Automatic backup created before restoration" in header:
                return True
    except:
        # If we can't read the file, assume it's not a backup
        pass
            
    return False


def create_backup_if_needed(target_dir, create_backup, is_backup, backup_path):
    """
    Create a backup snapshot if needed.
    
    Args:
        target_dir: Directory to backup
        create_backup: Whether to create a backup
        is_backup: Whether the source snapshot is a backup
        backup_path: Custom path for the backup file
        
    Returns:
        Path to the backup file if created, None otherwise
    """
    backup_file = None
    
    if create_backup and not is_backup:
        backup_file = create_backup_snapshot(target_dir, backup_path)
    elif create_backup and is_backup:
        print("Notice: Skipping backup creation since you're restoring from a backup file.")
    
    return backup_file


def create_backup_snapshot(target_dir: str, backup_path: str = None, comment: str = None) -> str:
    """
    Create a backup snapshot of the current state before restoration.
    
    Args:
        target_dir: Directory to snapshot
        backup_path: Custom path for the backup file
        comment: Optional comment to include in the backup
        
    Returns:
        Path to the created backup file
        
    Raises:
        RestoreError: If backup creation fails
    """
    try:
        print(f"Creating backup snapshot of current state...")
        
        # Use the create_snapshot function
        backup_dir = os.path.dirname(backup_path) if backup_path else os.path.join(target_dir, 'snapshots')
        
        # Generate a backup with a special prefix
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create the backup
        if backup_path:
            # If a specific backup path is provided, ensure its directory exists
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            auto_comment = "Automatic backup created before restoration" if comment is None else comment
            output_file = create_snapshot(target_dir, os.path.dirname(backup_path), None, auto_comment)
            # Rename to the specified file if needed
            if output_file != backup_path:
                os.rename(output_file, backup_path)
                output_file = backup_path
        else:
            # Default: create in snapshots directory with pre_restore prefix
            backup_dir = os.path.join(target_dir, 'snapshots')
            auto_comment = "Automatic backup created before restoration" if comment is None else comment
            output_file = create_snapshot(target_dir, 'snapshots', None, auto_comment)
            
            # Rename the file to indicate it's a pre-restore backup
            new_filename = os.path.join(backup_dir, f"pre_restore_backup_{timestamp}.md")
            os.rename(output_file, new_filename)
            output_file = new_filename
        
        print(f"Backup created at: {output_file}")
        return output_file
    except Exception as e:
        raise RestoreError(f"Failed to create backup snapshot: {str(e)}")


def display_snapshot_comment(comment):
    """
    Display the snapshot comment if present.
    
    Args:
        comment: Comment from the snapshot
    """
    if comment:
        print("\nSnapshot comment:")
        print(f"----------------")
        print(comment)
        print()


def restore_files(file_contents: Dict[str, str], target_dir: str, mode: str = 'overwrite') -> Tuple[int, int]:
    """
    Restore files based on content dictionary.
    
    Args:
        file_contents: Dictionary mapping file paths to content
        target_dir: Directory to restore to
        mode: Restoration mode (safe, overwrite, force)
        
    Returns:
        Tuple of (files_restored, files_skipped)
        
    Raises:
        RestoreError: If restoration fails
    """
    try:
        files_restored = 0
        files_skipped = 0
        
        for file_path, content in file_contents.items():
            if restore_single_file(file_path, content, target_dir, mode):
                files_restored += 1
            else:
                files_skipped += 1
                
        return files_restored, files_skipped
    except Exception as e:
        raise RestoreError(f"Error restoring files: {str(e)}")


def restore_single_file(file_path, content, target_dir, mode):
    """
    Restore a single file.
    
    Args:
        file_path: Path of the file relative to target_dir
        content: Content of the file
        target_dir: Directory to restore to
        mode: Restoration mode
        
    Returns:
        True if file was restored, False if skipped
    """
    # Skip binary file markers
    if content == "[Binary file - contents not shown]":
        print(f"Skipping binary file: {file_path}")
        return False
            
    full_path = os.path.join(target_dir, file_path)
    dir_path = os.path.dirname(full_path)
    
    # Create directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)
    
    file_exists = os.path.exists(full_path)
    
    if file_exists and mode == 'safe':
        print(f"Skipping existing file: {file_path}")
        return False
            
    # Write the file
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if file_exists:
        print(f"Overwritten: {file_path}")
    else:
        print(f"Created: {file_path}")
    
    return True


def print_restore_summary(files_restored, files_skipped, backup_file):
    """
    Print summary of the restoration.
    
    Args:
        files_restored: Number of files restored
        files_skipped: Number of files skipped
        backup_file: Path to the backup file if created
    """
    print(f"\nRestoration complete!")
    print(f"Files restored: {files_restored}")
    print(f"Files skipped: {files_skipped}")
    
    if backup_file:
        print(f"\nNote: A backup was created at {backup_file}")
        print(f"To undo this restoration, run: pkgmngr snapshot restore {backup_file}")


def selective_restore(snapshot_file_path: str, target_dir: str,
                     patterns: List[str] = None, exclude_patterns: List[str] = None,
                     interactive: bool = False, mode: str = 'overwrite',
                     create_backup: bool = True, backup_path: str = None) -> Optional[str]:
    """
    Selectively restore files from a snapshot based on patterns or interactive selection.
    
    Args:
        snapshot_file_path: Path to the snapshot file
        target_dir: Directory to restore to
        patterns: List of glob patterns to include (e.g. ['*.py', 'docs/*.md'])
        exclude_patterns: List of glob patterns to exclude
        interactive: Whether to prompt the user for each file
        mode: Restoration mode ('safe', 'overwrite', or 'force')
        create_backup: Whether to create a backup before restoring
        backup_path: Custom path for the backup file
        
    Returns:
        Path to the backup file if created, None otherwise
        
    Raises:
        RestoreError: If selective restoration fails
    """
    try:
        validate_restore_parameters(snapshot_file_path, target_dir, mode)
        
        # Ensure target directory exists
        os.makedirs(target_dir, exist_ok=True)
        
        # Check if we're restoring from a backup file
        is_backup = is_backup_snapshot(snapshot_file_path)
        
        # Create backup if requested and needed
        backup_file = create_backup_if_needed(target_dir, create_backup, is_backup, backup_path)
        
        # Parse the snapshot file
        file_contents, comment = parse_snapshot_file(snapshot_file_path)
        
        # Display comment if present
        display_snapshot_comment(comment)
        
        # Filter files based on patterns and user selection
        selected_files = select_files_for_restoration(file_contents, target_dir, patterns, 
                                                     exclude_patterns, interactive)
        
        # Restore the selected files
        print(f"\nRestoring {len(selected_files)} files to {target_dir}...")
        files_restored, files_skipped = restore_files(selected_files, target_dir, mode)
        
        # Print summary
        print_restore_summary(files_restored, files_skipped, backup_file)
        
        return backup_file
    except Exception as e:
        if isinstance(e, RestoreError):
            raise e
        else:
            raise RestoreError(f"Failed to perform selective restoration: {str(e)}")


def select_files_for_restoration(file_contents, target_dir, patterns, exclude_patterns, interactive):
    """
    Select files for restoration based on patterns and user interaction.
    
    Args:
        file_contents: Dictionary mapping file paths to content
        target_dir: Directory to restore to
        patterns: List of glob patterns to include
        exclude_patterns: List of glob patterns to exclude
        interactive: Whether to prompt the user for each file
        
    Returns:
        Dictionary of selected files and their contents
    """
    # Filter files based on patterns
    selected_files = filter_files_by_patterns(file_contents, patterns, exclude_patterns)
    
    # Interactive selection
    if interactive:
        selected_files = select_files_interactive(selected_files, target_dir)
    
    return selected_files


def filter_files_by_patterns(file_contents: Dict[str, str], 
                            patterns: List[str] = None, 
                            exclude_patterns: List[str] = None) -> Dict[str, str]:
    """
    Filter files based on inclusion and exclusion patterns.
    
    Args:
        file_contents: Dictionary mapping file paths to content
        patterns: List of glob patterns to include
        exclude_patterns: List of glob patterns to exclude
        
    Returns:
        Dictionary of filtered files
    """
    # Start with all files if no inclusion patterns provided
    if not patterns:
        selected_files = dict(file_contents)
    else:
        # Include only files that match at least one inclusion pattern
        selected_files = {}
        for file_path, content in file_contents.items():
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in patterns):
                selected_files[file_path] = content
    
    # Remove excluded files
    if exclude_patterns:
        for file_path in list(selected_files.keys()):
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude_patterns):
                del selected_files[file_path]
                
    return selected_files


def select_files_interactive(file_contents: Dict[str, str], target_dir: str) -> Dict[str, str]:
    """
    Let the user interactively select which files to restore.
    
    Args:
        file_contents: Dictionary mapping file paths to content
        target_dir: Directory to restore to
        
    Returns:
        Dictionary with selected files
    """
    print("Selecting files to restore:")
    print("--------------------------")
    
    # Sort files to display directories together
    file_list = sorted(file_contents.keys())
    final_selection = {}
    
    # Group files by directory for better organization
    dirs = group_files_by_directory(file_list)
    
    # Process by directory
    for dir_path, files in sorted(dirs.items()):
        print(f"\nDirectory: {dir_path or '.'}")
        
        # Ask if user wants to restore all files in this directory
        if len(files) > 1:
            response = input(f"  Restore all {len(files)} files in this directory? (y/n/q to quit): ").lower()
            if response == 'q':
                print("Restoration cancelled.")
                return final_selection
            
            if response in ('y', 'yes'):
                for file_path in files:
                    final_selection[file_path] = file_contents[file_path]
                continue
        
        # Ask for each file
        for file_path in files:
            process_interactive_file_selection(file_path, file_contents, target_dir, final_selection)
    
    return final_selection


def group_files_by_directory(file_list):
    """
    Group files by their directory.
    
    Args:
        file_list: List of file paths
        
    Returns:
        Dictionary mapping directory paths to lists of file paths
    """
    dirs = {}
    for file_path in file_list:
        dir_path = os.path.dirname(file_path)
        if dir_path not in dirs:
            dirs[dir_path] = []
        dirs[dir_path].append(file_path)
    return dirs


def process_interactive_file_selection(file_path, file_contents, target_dir, final_selection):
    """
    Process user selection for a single file.
    
    Args:
        file_path: Path of the file
        file_contents: Dictionary of all file contents
        target_dir: Target directory for restoration
        final_selection: Dictionary to update with selected files
        
    Returns:
        True to continue, False to quit
    """
    file_name = os.path.basename(file_path)
    full_path = os.path.join(target_dir, file_path)
    file_exists = os.path.exists(full_path)
    status = " (exists)" if file_exists else " (new)"
    
    # Skip binary files
    if file_contents[file_path] == "[Binary file - contents not shown]":
        print(f"  Skipping binary file: {file_name}")
        return True
    
    response = input(f"  Restore {file_name}{status}? (y/n/q to quit): ").lower()
    if response == 'q':
        print("Restoration cancelled.")
        return False
    
    if response in ('y', 'yes'):
        final_selection[file_path] = file_contents[file_path]
    
    return True