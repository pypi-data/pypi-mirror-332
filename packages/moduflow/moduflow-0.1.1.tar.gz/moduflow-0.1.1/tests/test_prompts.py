"""
Tests for the prompts module.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest
import yaml

from moduflow.prompts.templates import PromptGenerator
from moduflow.core.config import ConfigManager


class TestPromptGenerator(unittest.TestCase):
    """Tests for PromptGenerator."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Create necessary directories
        config_dir = self.test_dir / '.moduflow/config'
        sections_dir = config_dir / 'sections'
        self.design_dir = self.test_dir / 'design'
        
        config_dir.mkdir(parents=True)
        sections_dir.mkdir()
        self.design_dir.mkdir()
        
        # Create section configurations
        self.section1_config = {
            'name': 'section1',
            'description': 'Section 1 description',
            'files': ['section1/file1.py', 'section1/file2.py', 'shared.py']
        }
        
        self.section2_config = {
            'name': 'section2',
            'description': 'Section 2 description',
            'files': ['section2/file.py', 'shared.py']
        }
        
        with open(sections_dir / 'section1.yaml', 'w') as f:
            yaml.dump(self.section1_config, f)
        
        with open(sections_dir / 'section2.yaml', 'w') as f:
            yaml.dump(self.section2_config, f)
        
        # Create design files
        with open(self.design_dir / 'section1.md', 'w') as f:
            f.write('# Design for Section 1\n\nSection 1 design details.')
        
        with open(self.design_dir / 'section2.md', 'w') as f:
            f.write('# Design for Section 2\n\nSection 2 design details.')
        
        # Create files needed by the sections
        for section in ['section1', 'section2']:
            section_dir = self.test_dir / section
            section_dir.mkdir()
        
        with open(self.test_dir / 'section1/file1.py', 'w') as f:
            f.write('# Section 1 file 1')
        
        with open(self.test_dir / 'section1/file2.py', 'w') as f:
            f.write('# Section 1 file 2')
        
        with open(self.test_dir / 'section2/file.py', 'w') as f:
            f.write('# Section 2 file')
        
        with open(self.test_dir / 'shared.py', 'w') as f:
            f.write('# Shared file')
        
        # Create the prompt generator
        self.generator = PromptGenerator(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_generate_prompt(self):
        """Test generating a prompt."""
        # Generate the prompt
        prompt = self.generator.generate_prompt()
        
        # Check that the prompt contains important sections
        self.assertIn("# Section-Based Development Prompt", prompt)
        self.assertIn("## Project Overview", prompt)
        self.assertIn("## Development Guidelines", prompt)
        self.assertIn("## Section Details", prompt)
        
        # Check that the prompt contains section information
        self.assertIn("### section1", prompt)
        self.assertIn("Section 1 description", prompt)
        self.assertIn("### section2", prompt)
        self.assertIn("Section 2 description", prompt)
        
        # Check that the prompt contains design information
        self.assertIn("Design for Section 1", prompt)
        self.assertIn("Design for Section 2", prompt)
        
        # Check that the prompt contains file information
        self.assertIn("section1/file1.py", prompt)
        self.assertIn("section1/file2.py", prompt)
        self.assertIn("section2/file.py", prompt)
        self.assertIn("shared.py", prompt)
        
        # Check that the prompt includes information about files used by multiple sections
        self.assertIn("Files Used By Multiple Sections", prompt)
        self.assertIn("shared.py", prompt)
    
    def test_prompt_with_missing_design_file(self):
        """Test generating a prompt when a design file is missing."""
        # Remove a design file
        (self.design_dir / 'section1.md').unlink()
        
        # Generate the prompt
        prompt = self.generator.generate_prompt()
        
        # Check that the prompt still includes the section
        self.assertIn("### section1", prompt)
        self.assertIn("Section 1 description", prompt)
        
        # But it shouldn't contain the design file content
        self.assertNotIn("Design for Section 1", prompt)
    
    def test_prompt_with_missing_files(self):
        """Test generating a prompt when files are missing."""
        # Remove a file
        (self.test_dir / 'section1/file1.py').unlink()
        
        # Generate the prompt
        prompt = self.generator.generate_prompt()
        
        # The file should still be listed, but marked as missing
        self.assertIn("section1/file1.py", prompt)
        self.assertIn("missing", prompt.lower())
    
    def test_prompt_with_no_sections(self):
        """Test generating a prompt when no sections exist."""
        # Remove all section configurations
        config_dir = self.test_dir / '.moduflow/config/sections'
        for file in config_dir.glob('*.yaml'):
            file.unlink()
        
        # Generate the prompt
        prompt = self.generator.generate_prompt()
        
        # The prompt should still contain the basic structure
        self.assertIn("# Section-Based Development Prompt", prompt)
        self.assertIn("## Project Overview", prompt)
        self.assertIn("## Development Guidelines", prompt)
        
        # But it shouldn't contain section details
        self.assertNotIn("## Section Details", prompt)
        self.assertNotIn("### section1", prompt)
        self.assertNotIn("### section2", prompt)
    
    def test_get_base_prompt(self):
        """Test getting the base prompt."""
        # Get the base prompt
        base_prompt = self.generator._get_base_prompt()
        
        # Check that it contains the expected sections
        self.assertIn("# Section-Based Development Prompt", base_prompt)
        self.assertIn("## Project Overview", base_prompt)
        self.assertIn("## Development Guidelines", base_prompt)
        self.assertIn("Test-Driven Development", base_prompt)
        self.assertIn("Section Isolation", base_prompt)
        self.assertIn("File Organization", base_prompt)
        self.assertIn("Implementation Process", base_prompt)
    
    def test_get_closing_instructions(self):
        """Test getting the closing instructions."""
        # Get the closing instructions
        closing = self.generator._get_closing_instructions()
        
        # Check that it contains the expected sections
        self.assertIn("## Deliverables", closing)
        self.assertIn("## Additional Notes", closing)
        self.assertIn("Test files", closing)
        self.assertIn("Implementation files", closing)
        self.assertIn("Documentation", closing)


if __name__ == "__main__":
    unittest.main()