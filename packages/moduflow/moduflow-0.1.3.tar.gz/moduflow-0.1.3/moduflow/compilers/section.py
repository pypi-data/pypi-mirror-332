"""
Section compilation for ModuFlow.

This module provides functionality for compiling sections.
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Set

from moduflow.core.config import ConfigManager
from moduflow.core.paths import PathManager
from moduflow.handlers.file_handler import FileHandler


class SectionCompiler:
    """Compiler for sections."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the section compiler.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
        self.config_manager = ConfigManager(project_root)
        self.path_manager = PathManager(project_root)
        self.file_handler = FileHandler(project_root)
    
    def compile_section(self, name: str) -> Path:
        """Compile a section.
        
        Args:
            name: Name of the section.
            
        Returns:
            Path to the compiled section.
            
        Raises:
            FileNotFoundError: If the section doesn't exist.
        """
        # Read section configuration
        section_config = self.config_manager.read_section_config(name)
        
        # Create output directory
        section_dir = self.path_manager.get_section_output_dir(name)
        if section_dir.exists():
            shutil.rmtree(section_dir)
        section_dir.mkdir(parents=True)
        
        # Copy files
        copied_files = self.file_handler.copy_files(
            section_config.get('files', []),
            self.project_root,
            section_dir,
            skip_missing=True
        )
        
        # Copy design files
        design_files = list(self.path_manager.design_dir.glob(f"{name}*"))
        if design_files:
            design_output_dir = section_dir / "design"
            design_output_dir.mkdir(exist_ok=True)
            
            for design_file in design_files:
                try:
                    shutil.copy2(design_file, design_output_dir / design_file.name)
                except Exception as e:
                    print(f"Warning: Could not copy design file {design_file}: {e}")
        
        # Create a manifest file
        manifest = {
            'name': name,
            'description': section_config.get('description', ''),
            'files': copied_files,
            'design_files': [f.name for f in design_files]
        }
        
        manifest_path = section_dir / "manifest.yaml"
        self.file_handler.save_yaml(manifest, manifest_path)
        
        return section_dir
    
    def compile_all_sections(self) -> Dict[str, Path]:
        """Compile all sections.
        
        Returns:
            Dictionary mapping section names to their compiled directories.
        """
        # Clear the output directory
        if self.path_manager.output_dir.exists():
            shutil.rmtree(self.path_manager.output_dir)
        self.path_manager.output_dir.mkdir()
        
        # Get all sections
        sections = self.config_manager.read_all_section_configs()
        
        # Compile each section
        compiled_sections = {}
        for section_name in sections:
            try:
                compiled_dir = self.compile_section(section_name)
                compiled_sections[section_name] = compiled_dir
            except Exception as e:
                print(f"Error compiling section '{section_name}': {e}")
        
        return compiled_sections
    
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