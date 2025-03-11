"""
Project compilation for ModuFlow.

This module provides functionality for compiling entire projects.
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Set

from moduflow.core.config import ConfigManager
from moduflow.core.paths import PathManager
from moduflow.handlers.file_handler import FileHandler


class ProjectCompiler:
    """Compiler for entire projects."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the project compiler.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
        self.config_manager = ConfigManager(project_root)
        self.path_manager = PathManager(project_root)
        self.file_handler = FileHandler(project_root)
    
    def compile_project(self) -> Path:
        """Compile the entire project.
        
        Returns:
            Path to the compiled project.
        """
        # Create output directory
        project_dir = self.path_manager.get_project_output_dir()
        if project_dir.exists():
            shutil.rmtree(project_dir)
        project_dir.mkdir(parents=True)
        
        # Get all sections
        sections = self.config_manager.read_all_section_configs()
        
        # Track which files have been copied to avoid duplicates
        copied_files = set()
        
        # Copy files from all sections
        for section_name, section_config in sections.items():
            for file_path in section_config.get('files', []):
                if file_path in copied_files:
                    continue
                
                src_path = self.project_root / file_path
                dest_path = project_dir / file_path
                
                if not src_path.exists():
                    print(f"Warning: File {file_path} does not exist. Skipping.")
                    continue
                
                # Create destination directory
                dest_path.parent.mkdir(exist_ok=True, parents=True)
                
                # Copy the file
                try:
                    shutil.copy2(src_path, dest_path)
                    copied_files.add(file_path)
                except Exception as e:
                    print(f"Error copying file {file_path}: {e}")
        
        # Create a combined design directory
        design_dir = project_dir / "design"
        design_dir.mkdir(exist_ok=True)
        
        # Copy all design files
        for design_file in self.path_manager.design_dir.glob("*.md"):
            try:
                shutil.copy2(design_file, design_dir / design_file.name)
            except Exception as e:
                print(f"Error copying design file {design_file}: {e}")
        
        # Create a manifest file
        manifest = {
            'project_name': self.project_root.name,
            'sections': list(sections.keys()),
            'files': sorted(list(copied_files)),
            'design_files': [f.name for f in self.path_manager.design_dir.glob("*.md")]
        }
        
        manifest_path = project_dir / "manifest.yaml"
        self.save_yaml(manifest, manifest_path)
        
        return project_dir
    
    def save_yaml(self, data: Dict[str, Any], file_path: Path) -> None:
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