"""
YAML handling for ModuFlow.

This module provides utilities for working with YAML files.
"""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional, TextIO


class YamlHandler:
    """Handler for YAML operations."""
    
    @staticmethod
    def load_yaml(file_path: Path) -> Dict[str, Any]:
        """Load a YAML file.
        
        Args:
            file_path: Path to the YAML file.
            
        Returns:
            Dictionary containing the YAML data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            yaml.YAMLError: If the YAML is invalid.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"YAML file not found: {file_path}")
        
        with open(file_path, 'r') as f:
            return yaml.safe_load(f) or {}
    
    @staticmethod
    def save_yaml(data: Dict[str, Any], file_path: Path) -> None:
        """Save data to a YAML file.
        
        Args:
            data: Dictionary to save.
            file_path: Path to the YAML file.
            
        Raises:
            yaml.YAMLError: If the data cannot be serialized to YAML.
        """
        # Ensure parent directory exists
        file_path.parent.mkdir(exist_ok=True, parents=True)
        
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    @staticmethod
    def merge_yaml(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Merge two YAML dictionaries.
        
        Args:
            base: Base dictionary.
            override: Dictionary to merge on top of base.
            
        Returns:
            Merged dictionary.
        """
        result = base.copy()
        
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge nested dictionaries
                result[key] = YamlHandler.merge_yaml(result[key], value)
            else:
                # Override or add value
                result[key] = value
        
        return result
    
    @staticmethod
    def yaml_to_string(data: Dict[str, Any]) -> str:
        """Convert a dictionary to a YAML string.
        
        Args:
            data: Dictionary to convert.
            
        Returns:
            YAML string.
        """
        return yaml.dump(data, default_flow_style=False, sort_keys=False)
    
    @staticmethod
    def string_to_yaml(yaml_str: str) -> Dict[str, Any]:
        """Convert a YAML string to a dictionary.
        
        Args:
            yaml_str: YAML string to convert.
            
        Returns:
            Dictionary containing the YAML data.
            
        Raises:
            yaml.YAMLError: If the YAML is invalid.
        """
        return yaml.safe_load(yaml_str) or {}