"""
Configuration management for ModuFlow.

This module provides functionality for working with YAML configuration files,
including reading, writing, and merging section configurations.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional

# Constants
CONFIG_DIR = '.moduflow/config'
SECTIONS_DIR = 'sections'
COMPILED_CONFIG = 'compiled.yaml'


class ConfigManager:
    """Manager for ModuFlow configuration files."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the configuration manager.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
        self.config_dir = self.project_root / CONFIG_DIR
        self.sections_dir = self.config_dir / SECTIONS_DIR
        self.compiled_path = self.config_dir / COMPILED_CONFIG
    
    def init_config(self) -> None:
        """Initialize the configuration directory structure."""
        # Create config directories
        self.config_dir.mkdir(exist_ok=True, parents=True)
        self.sections_dir.mkdir(exist_ok=True, parents=True)
        
        # Create empty compiled config if it doesn't exist
        if not self.compiled_path.exists():
            self.write_compiled_config({'sections': {}})
    
    def read_section_config(self, section_name: str) -> Dict[str, Any]:
        """Read a section configuration file.
        
        Args:
            section_name: Name of the section.
            
        Returns:
            Dictionary containing the section configuration.
        
        Raises:
            FileNotFoundError: If the section config doesn't exist.
        """
        section_path = self.sections_dir / f"{section_name}.yaml"
        
        if not section_path.exists():
            raise FileNotFoundError(f"Section configuration for '{section_name}' not found")
        
        with open(section_path, 'r') as f:
            return yaml.safe_load(f) or {}
    
    def read_all_section_configs(self) -> Dict[str, Dict[str, Any]]:
        """Read all section configuration files.
        
        Returns:
            Dictionary mapping section names to their configurations.
        """
        sections = {}
        
        for section_file in self.sections_dir.glob('*.yaml'):
            section_name = section_file.stem
            try:
                section_config = self.read_section_config(section_name)
                sections[section_name] = section_config
            except Exception as e:
                print(f"Error reading section '{section_name}': {e}")
        
        return sections
    
    def write_section_config(self, section_name: str, config: Dict[str, Any]) -> None:
        """Write a section configuration file.
        
        Args:
            section_name: Name of the section.
            config: Dictionary containing the section configuration.
        """
        # Ensure the sections directory exists
        self.sections_dir.mkdir(exist_ok=True, parents=True)
        
        section_path = self.sections_dir / f"{section_name}.yaml"
        
        with open(section_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
    
    def read_compiled_config(self) -> Dict[str, Any]:
        """Read the compiled configuration file.
        
        Returns:
            Dictionary containing the compiled configuration.
        """
        if not self.compiled_path.exists():
            return {'sections': {}}
        
        with open(self.compiled_path, 'r') as f:
            return yaml.safe_load(f) or {'sections': {}}
    
    def write_compiled_config(self, config: Dict[str, Any]) -> None:
        """Write the compiled configuration file.
        
        Args:
            config: Dictionary containing the compiled configuration.
        """
        # Ensure the config directory exists
        self.config_dir.mkdir(exist_ok=True, parents=True)
        
        with open(self.compiled_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
    
    def compile_config(self) -> Dict[str, Any]:
        """Compile all section configurations into a single configuration.
        
        Returns:
            Dictionary containing the compiled configuration.
        """
        sections = self.read_all_section_configs()
        compiled = {'sections': {}}
        
        for section_name, section_config in sections.items():
            compiled['sections'][section_name] = section_config
        
        # Write the compiled configuration
        self.write_compiled_config(compiled)
        
        return compiled
    
    def find_files_in_multiple_sections(self) -> Dict[str, List[str]]:
        """Find files that are used in multiple sections.
        
        Returns:
            Dictionary mapping file paths to lists of section names.
        """
        file_usage = {}
        sections = self.read_all_section_configs()
        
        for section_name, section_config in sections.items():
            for file_path in section_config.get('files', []):
                if file_path not in file_usage:
                    file_usage[file_path] = []
                file_usage[file_path].append(section_name)
        
        # Filter to only files used in multiple sections
        return {file: sections for file, sections in file_usage.items() if len(sections) > 1}
    
    def add_file_to_sections(self, file_path: str, section_names: List[str]) -> None:
        """Add a file to multiple sections.
        
        Args:
            file_path: Path to the file.
            section_names: List of section names.
        """
        for section_name in section_names:
            try:
                config = self.read_section_config(section_name)
                
                if 'files' not in config:
                    config['files'] = []
                
                if file_path not in config['files']:
                    config['files'].append(file_path)
                
                self.write_section_config(section_name, config)
                
            except FileNotFoundError:
                print(f"Section '{section_name}' does not exist. Skipping.")
        
        # Recompile the configuration
        self.compile_config()