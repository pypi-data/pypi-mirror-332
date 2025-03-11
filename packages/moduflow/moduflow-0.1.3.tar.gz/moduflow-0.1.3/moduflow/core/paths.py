"""
Path management for ModuFlow.

This module provides utilities for working with paths in ModuFlow projects.
"""

import os
from pathlib import Path
from typing import Optional


class PathManager:
    """Manager for paths in a ModuFlow project."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the path manager.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
        
        # Define standard directories
        self.config_dir = self.project_root / '.moduflow/config'
        self.sections_dir = self.config_dir / 'sections'
        self.output_dir = self.project_root / '.compiled_sections'
        self.design_dir = self.project_root / 'design'
    
    def ensure_directories(self) -> None:
        """Ensure that all required directories exist."""
        self.config_dir.mkdir(exist_ok=True, parents=True)
        self.sections_dir.mkdir(exist_ok=True, parents=True)
        self.output_dir.mkdir(exist_ok=True, parents=True)
        self.design_dir.mkdir(exist_ok=True, parents=True)
    
    def get_section_config_path(self, section_name: str) -> Path:
        """Get the path to a section configuration file.
        
        Args:
            section_name: Name of the section.
            
        Returns:
            Path to the section configuration file.
        """
        return self.sections_dir / f"{section_name}.yaml"
    
    def get_compiled_config_path(self) -> Path:
        """Get the path to the compiled configuration file.
        
        Returns:
            Path to the compiled configuration file.
        """
        return self.config_dir / "compiled.yaml"
    
    def get_section_output_dir(self, section_name: str) -> Path:
        """Get the output directory for a section.
        
        Args:
            section_name: Name of the section.
            
        Returns:
            Path to the section output directory.
        """
        return self.output_dir / section_name
    
    def get_project_output_dir(self) -> Path:
        """Get the output directory for the entire project.
        
        Returns:
            Path to the project output directory.
        """
        return self.output_dir / "project"
    
    def get_design_file_path(self, section_name: str) -> Path:
        """Get the path to a section design file.
        
        Args:
            section_name: Name of the section.
            
        Returns:
            Path to the section design file.
        """
        return self.design_dir / f"{section_name}.md"
    
    def get_file_paths_by_pattern(self, pattern: str) -> list[Path]:
        """Get paths to files matching a pattern.
        
        Args:
            pattern: Glob pattern to match files.
            
        Returns:
            List of matching file paths.
        """
        return list(self.project_root.glob(pattern))
    
    def get_relative_path(self, path: Path) -> str:
        """Get a path relative to the project root.
        
        Args:
            path: Absolute path.
            
        Returns:
            Path relative to the project root.
        """
        return str(path.relative_to(self.project_root))