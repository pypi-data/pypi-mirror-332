"""
File operations for ModuFlow.

This module provides utilities for working with files in a ModuFlow project.
"""

import os
import shutil
from pathlib import Path
from typing import List, Optional


class FileHandler:
    """Handler for file operations."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the file handler.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
    
    def ensure_directory(self, directory: Path) -> None:
        """Ensure a directory exists.
        
        Args:
            directory: Path to the directory.
        """
        directory.mkdir(exist_ok=True, parents=True)
    
    def copy_file(self, source: Path, destination: Path) -> None:
        """Copy a file.
        
        Args:
            source: Path to the source file.
            destination: Path to the destination file.
            
        Raises:
            FileNotFoundError: If the source file doesn't exist.
        """
        if not source.exists():
            raise FileNotFoundError(f"Source file not found: {source}")
        
        # Ensure parent directory exists
        destination.parent.mkdir(exist_ok=True, parents=True)
        
        shutil.copy2(source, destination)
    
    def copy_files(self, files: List[str], source_dir: Path, dest_dir: Path, 
                   skip_missing: bool = True) -> List[str]:
        """Copy multiple files.
        
        Args:
            files: List of file paths relative to source_dir.
            source_dir: Source directory.
            dest_dir: Destination directory.
            skip_missing: If True, skip missing files. If False, raise FileNotFoundError.
            
        Returns:
            List of files that were copied.
            
        Raises:
            FileNotFoundError: If skip_missing is False and a file doesn't exist.
        """
        copied_files = []
        
        for file_path in files:
            src_path = source_dir / file_path
            dest_path = dest_dir / file_path
            
            if not src_path.exists():
                if skip_missing:
                    print(f"Warning: File {file_path} does not exist. Skipping.")
                    continue
                else:
                    raise FileNotFoundError(f"File not found: {src_path}")
            
            # Ensure parent directory exists
            dest_path.parent.mkdir(exist_ok=True, parents=True)
            
            # Copy the file
            shutil.copy2(src_path, dest_path)
            copied_files.append(file_path)
        
        return copied_files
    
    def list_files(self, directory: Path, pattern: str = "*") -> List[Path]:
        """List files in a directory.
        
        Args:
            directory: Directory to list files from.
            pattern: Glob pattern to match files.
            
        Returns:
            List of file paths.
        """
        return list(directory.glob(pattern))
    
    def find_files_by_extension(self, directory: Path, extensions: List[str]) -> List[Path]:
        """Find files with specific extensions.
        
        Args:
            directory: Directory to search in.
            extensions: List of file extensions (without the dot).
            
        Returns:
            List of file paths.
        """
        files = []
        for ext in extensions:
            files.extend(directory.glob(f"**/*.{ext}"))
        return files
    
    def save_yaml(self, data: dict, file_path: Path) -> None:
        """Save data to a YAML file.
        
        Args:
            data: Dictionary to save.
            file_path: Path to the YAML file.
        """
        import yaml
        
        # Ensure parent directory exists
        file_path.parent.mkdir(exist_ok=True, parents=True)
        
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    def update_gitignore(self, entries: List[str]) -> bool:
        """Add entries to .gitignore.
        
        Args:
            entries: List of entries to add.
            
        Returns:
            True if the file was updated, False otherwise.
        """
        gitignore_path = self.project_root / '.gitignore'
        
        # Read existing content
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                content = f.read()
            
            # Check if all entries are already in the file
            missing_entries = [entry for entry in entries if entry not in content]
            
            if not missing_entries:
                return False  # No updates needed
            
            # Add missing entries
            new_content = content
            if not content.endswith('\n'):
                new_content += '\n'
            
            new_content += "\n# ModuFlow entries\n"
            for entry in missing_entries:
                new_content += f"{entry}\n"
        else:
            # Create new file
            new_content = "# ModuFlow entries\n"
            for entry in entries:
                new_content += f"{entry}\n"
        
        # Write updated content
        with open(gitignore_path, 'w') as f:
            f.write(new_content)
        
        return True  # File was updated