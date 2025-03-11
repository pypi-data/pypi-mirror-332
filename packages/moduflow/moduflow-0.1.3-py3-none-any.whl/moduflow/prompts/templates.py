"""
Prompt templates for ModuFlow.

This module provides templates for generating AI development prompts.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional, List

from moduflow.core.config import ConfigManager


class PromptGenerator:
    """Generator for AI development prompts."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the prompt generator.
        
        Args:
            project_root: Path to the project root. If None, uses current directory.
        """
        self.project_root = Path(project_root or os.getcwd()).resolve()
        self.config_manager = ConfigManager(project_root)
        self.design_dir = self.project_root / 'design'
    
    def generate_prompt(self) -> str:
        """Generate an AI development prompt based on the project configuration.
        
        Returns:
            The generated prompt.
        """
        prompt = self._get_base_prompt()
        
        # Add section details
        sections = self.config_manager.read_all_section_configs()
        if sections:
            prompt += "\n## Section Details\n"
            
            for section_name, section_config in sections.items():
                prompt += f"\n### {section_name}\n"
                
                if section_config.get('description'):
                    prompt += f"{section_config['description']}\n\n"
                
                # Check if there's a design document
                design_file = self.design_dir / f"{section_name}.md"
                if design_file.exists():
                    try:
                        with open(design_file, 'r') as f:
                            design_content = f.read()
                        prompt += f"**Design Document:**\n\n```markdown\n{design_content}\n```\n\n"
                    except Exception as e:
                        prompt += f"*Error reading design file: {e}*\n\n"
                
                prompt += "**Files in this section:**\n\n"
                for file_path in section_config.get('files', []):
                    file_exists = (self.project_root / file_path).exists()
                    status = "" if file_exists else " (missing)"
                    prompt += f"- `{file_path}`{status}\n"
                
                prompt += "\n"
        
        # Add shared files info
        shared_files = self.config_manager.find_files_in_multiple_sections()
        if shared_files:
            prompt += "\n## Files Used By Multiple Sections\n"
            prompt += "These files are used by multiple sections and should be handled with care:\n\n"
            
            for file_path, section_names in shared_files.items():
                sections_str = ", ".join(section_names)
                prompt += f"- `{file_path}` (used by: {sections_str})\n"
        
        # Add final instructions
        prompt += self._get_closing_instructions()
        
        return prompt
    
    def _get_base_prompt(self) -> str:
        """Get the base prompt template.
        
        Returns:
            The base prompt template.
        """
        return """
# Section-Based Development Prompt

## Project Overview
You are tasked with implementing a section-based development approach for this project. The project is divided into logical sections, each containing related files. Your goal is to develop these sections using Test-Driven Development (TDD).

## Development Guidelines

1. **Test-Driven Development (TDD)**:
   - Write tests before implementing functionality
   - Tests should be comprehensive and cover edge cases
   - Each section should have its own test suite

2. **Section Isolation**:
   - Each section should be as independent as possible
   - Shared code should be minimized and clearly documented
   - When a section depends on another section, document this dependency

3. **File Organization**:
   - Group files by section
   - Use consistent naming conventions
   - Add new files to the appropriate section in the configuration

4. **Implementation Process**:
   - Review the design document for the section
   - Implement tests according to the requirements
   - Implement the functionality to pass the tests
   - Document any design decisions or trade-offs
   - Update the section configuration if new files are created
"""
    
    def _get_closing_instructions(self) -> str:
        """Get the closing instructions for the prompt.
        
        Returns:
            The closing instructions.
        """
        return """
## Deliverables

For each section you work on, you should provide:

1. Test files implementing the requirements
2. Implementation files that pass the tests
3. Documentation of design decisions and usage instructions
4. Any updates to the section configuration

## Additional Notes

- The project uses YAML files to track which files belong to which sections
- The output directory `.compiled_sections` contains compiled versions of each section
- Follow the existing code style and conventions
- If you create new files, add them to the appropriate section configuration
- Use the ModuFlow tool to manage sections and compilation
"""