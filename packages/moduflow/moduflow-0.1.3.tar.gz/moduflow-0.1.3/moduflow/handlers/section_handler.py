"""
Section management for ModuFlow.

This module provides functionality for working with sections, including
creating, updating, and compiling sections.
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Set

from moduflow.core.config import ConfigManager
from moduflow.core.paths import PathManager


class SectionHandler:
    """Handler for section operations."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the section handler.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
        self.config_manager = ConfigManager(project_root)
        self.path_manager = PathManager(project_root)
        
    def init_project(self) -> None:
        """Initialize a new project structure."""
        # Initialize configuration
        self.config_manager.init_config()
        
        # Ensure directories exist
        self.path_manager.ensure_directories()
        
        # Update .gitignore
        gitignore_path = self.project_root / '.gitignore'
        gitignore_entries = [
            '.compiled_sections/',
            '.moduflow/'
        ]
        
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                content = f.read()
            
            # Add any missing entries
            new_content = content
            for entry in gitignore_entries:
                if entry not in content:
                    new_content += f"\n# ModuFlow directories\n{entry}\n"
            
            # Only write if changes were made
            if new_content != content:
                with open(gitignore_path, 'w') as f:
                    f.write(new_content)
        else:
            with open(gitignore_path, 'w') as f:
                f.write("\n# ModuFlow directories\n")
                for entry in gitignore_entries:
                    f.write(f"{entry}\n")
        
        print(f"Project initialized for section-based development at {self.project_root}")
    
    def create_section(self, name: str, description: str = "", files: Optional[List[str]] = None) -> None:
        """Create a new section.
        
        Args:
            name: Name of the section.
            description: Description of the section.
            files: Optional list of files to include in the section.
        """
        # Check if section already exists
        try:
            self.config_manager.read_section_config(name)
            print(f"Section '{name}' already exists.")
            return
        except FileNotFoundError:
            pass
        
        # Create the section configuration
        config = {
            'name': name,
            'description': description,
            'files': files or []
        }
        
        # Write the section configuration
        self.config_manager.write_section_config(name, config)
        
        # Create a design file for the section
        design_file = self.path_manager.get_design_file_path(name)
        if not design_file.exists():
            with open(design_file, 'w') as f:
                f.write(f"# Design for {name}\n\n")
                if description:
                    f.write(f"{description}\n\n")
        
        # Recompile the configuration
        self.config_manager.compile_config()
        
        print(f"Created section '{name}'")
    
    def update_section(self, name: str, description: Optional[str] = None, 
                       files: Optional[List[str]] = None) -> None:
        """Update an existing section.
        
        Args:
            name: Name of the section.
            description: New description of the section (if provided).
            files: New list of files (if provided).
        """
        try:
            config = self.config_manager.read_section_config(name)
            
            if description is not None:
                config['description'] = description
            
            if files is not None:
                config['files'] = files
            
            self.config_manager.write_section_config(name, config)
            
            # Recompile the configuration
            self.config_manager.compile_config()
            
            print(f"Updated section '{name}'")
            
        except FileNotFoundError:
            print(f"Section '{name}' does not exist. Use create-section to create it.")
    
    def add_files_to_section(self, name: str, files: List[str]) -> None:
        """Add files to an existing section.
        
        Args:
            name: Name of the section.
            files: List of files to add.
        """
        try:
            config = self.config_manager.read_section_config(name)
            
            if 'files' not in config:
                config['files'] = []
            
            # Add new files (avoiding duplicates)
            current_files = set(config['files'])
            current_files.update(files)
            config['files'] = sorted(current_files)
            
            self.config_manager.write_section_config(name, config)
            
            # Recompile the configuration
            self.config_manager.compile_config()
            
            print(f"Added files to section '{name}'")
            
        except FileNotFoundError:
            print(f"Section '{name}' does not exist. Use create-section to create it.")
    
    def compile_section(self, name: str) -> None:
        """Compile a section to the output directory.
        
        Args:
            name: Name of the section to compile.
        """
        try:
            config = self.config_manager.read_section_config(name)
            
            # Create output directory for the section
            section_dir = self.path_manager.get_section_output_dir(name)
            if section_dir.exists():
                shutil.rmtree(section_dir)
            section_dir.mkdir(parents=True)
            
            # Copy files
            for file_path in config.get('files', []):
                src_path = self.project_root / file_path
                if not src_path.exists():
                    print(f"Warning: File {file_path} does not exist. Skipping.")
                    continue
                
                # Create destination directory structure
                dest_path = section_dir / file_path
                dest_path.parent.mkdir(exist_ok=True, parents=True)
                
                # Copy the file
                shutil.copy2(src_path, dest_path)
            
            # Copy design files
            design_files = list(self.path_manager.design_dir.glob(f"{name}*"))
            if design_files:
                design_output_dir = section_dir / "design"
                design_output_dir.mkdir(exist_ok=True)
                
                for design_file in design_files:
                    shutil.copy2(design_file, design_output_dir / design_file.name)
            
            print(f"Compiled section '{name}' to {section_dir}")
            
        except FileNotFoundError:
            print(f"Section '{name}' does not exist.")
    
    def compile_all_sections(self) -> None:
        """Compile all sections to the output directory."""
        # Clear the output directory
        if self.path_manager.output_dir.exists():
            shutil.rmtree(self.path_manager.output_dir)
        self.path_manager.output_dir.mkdir()
        
        # Get all sections
        sections = self.config_manager.read_all_section_configs()
        
        # Compile each section
        for section_name in sections:
            self.compile_section(section_name)
        
        print(f"All sections compiled to {self.path_manager.output_dir}")
    
    def compile_project(self) -> None:
        """Compile the entire project to a single directory structure."""
        project_dir = self.path_manager.get_project_output_dir()
        if project_dir.exists():
            shutil.rmtree(project_dir)
        project_dir.mkdir(parents=True)
        
        # Get all sections
        sections = self.config_manager.read_all_section_configs()
        
        # Copy all files (without duplicating)
        copied_files = set()
        
        for section_name, section_config in sections.items():
            for file_path in section_config.get('files', []):
                if file_path in copied_files:
                    continue
                
                src_path = self.project_root / file_path
                if not src_path.exists():
                    print(f"Warning: File {file_path} does not exist. Skipping.")
                    continue
                
                # Create destination directory structure
                dest_path = project_dir / file_path
                dest_path.parent.mkdir(exist_ok=True, parents=True)
                
                # Copy the file
                shutil.copy2(src_path, dest_path)
                copied_files.add(file_path)
        
        print(f"Project compiled to {project_dir}")
    
    def list_sections(self) -> None:
        """List all sections and their files."""
        sections = self.config_manager.read_all_section_configs()
        
        if not sections:
            print("No sections defined yet.")
            return
        
        for section_name, section_config in sections.items():
            file_count = len(section_config.get('files', []))
            print(f"\n{section_name} ({file_count} files):")
            
            if section_config.get('description'):
                print(f"  Description: {section_config['description']}")
            
            if file_count > 0:
                print("  Files:")
                for file_path in section_config.get('files', []):
                    file_exists = (self.project_root / file_path).exists()
                    status = "" if file_exists else " (missing)"
                    print(f"    - {file_path}{status}")
        
        # Find files used by multiple sections
        shared_files = self.config_manager.find_files_in_multiple_sections()
        
        if shared_files:
            print("\nFiles used by multiple sections:")
            for file_path, section_names in shared_files.items():
                sections_str = ", ".join(section_names)
                print(f"  - {file_path} → {sections_str}")
    
    def analyze_project(self) -> None:
        """Analyze the project structure and suggest sections."""
        suggested_sections = {}
        
        # Walk through the project directory
        for root, dirs, files in os.walk(self.project_root):
            # Skip the output directory, config directory, and hidden directories
            rel_root = os.path.relpath(root, self.project_root)
            if (rel_root.startswith('.compiled_sections') or 
                rel_root.startswith('.moduflow') or 
                rel_root.startswith('.')):
                continue
            
            # Skip virtual environments, node_modules, etc.
            if any(d in rel_root for d in ['venv', 'env', 'node_modules', '__pycache__']):
                continue
            
            # If we're at a top-level directory or a module directory (contains __init__.py)
            if rel_root == '.' or '__init__.py' in files:
                # Determine the section name
                if rel_root == '.':
                    section_name = 'core'
                else:
                    section_name = rel_root.replace(os.path.sep, '_')
                
                # Skip if this would be an empty section
                if not files:
                    continue
                
                # Add files to the suggested section
                if section_name not in suggested_sections:
                    suggested_sections[section_name] = []
                
                for file in files:
                    # Skip hidden files and compiled files
                    if file.startswith('.') or file.endswith(('.pyc', '.pyo')):
                        continue
                    
                    file_path = os.path.join(rel_root, file)
                    if rel_root == '.':
                        file_path = file
                    
                    suggested_sections[section_name].append(file_path)
        
        # Output suggestions
        print("Suggested sections based on project structure:")
        for section_name, files in suggested_sections.items():
            print(f"\n{section_name} ({len(files)} files):")
            for file in files[:5]:  # Show only first 5 files
                print(f"  - {file}")
            if len(files) > 5:
                print(f"  - ... and {len(files) - 5} more files")
        
        print("\nUse 'create-section' to add these sections to your project.")