"""
Tests for the compilers module.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest
import yaml

from moduflow.compilers.section import SectionCompiler
from moduflow.compilers.project import ProjectCompiler
from moduflow.core.config import ConfigManager
from moduflow.core.paths import PathManager


class TestSectionCompiler(unittest.TestCase):
    """Tests for SectionCompiler."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Create necessary directories
        config_dir = self.test_dir / '.moduflow/config'
        sections_dir = config_dir / 'sections'
        self.output_dir = self.test_dir / '.compiled_sections'
        self.design_dir = self.test_dir / 'design'
        
        config_dir.mkdir(parents=True)
        sections_dir.mkdir()
        self.output_dir.mkdir()
        self.design_dir.mkdir()
        
        # Create section configuration
        self.section_config = {
            'name': 'test',
            'description': 'Test section',
            'files': ['test/file1.py', 'test/file2.py', 'shared.py']
        }
        
        with open(sections_dir / 'test.yaml', 'w') as f:
            yaml.dump(self.section_config, f)
        
        # Create test files
        test_dir = self.test_dir / 'test'
        test_dir.mkdir()
        
        with open(self.test_dir / 'test/file1.py', 'w') as f:
            f.write('# Test file 1')
        
        with open(self.test_dir / 'test/file2.py', 'w') as f:
            f.write('# Test file 2')
        
        with open(self.test_dir / 'shared.py', 'w') as f:
            f.write('# Shared file')
        
        # Create design file
        with open(self.design_dir / 'test.md', 'w') as f:
            f.write('# Design for test section')
        
        # Create section compiler
        self.compiler = SectionCompiler(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_compile_section(self):
        """Test compiling a section."""
        # Compile the section
        output_dir = self.compiler.compile_section('test')
        
        # Check that the output directory was created
        self.assertTrue(output_dir.exists())
        
        # Check that all files were copied
        self.assertTrue((output_dir / 'test/file1.py').exists())
        self.assertTrue((output_dir / 'test/file2.py').exists())
        self.assertTrue((output_dir / 'shared.py').exists())
        
        # Check that the design file was copied
        self.assertTrue((output_dir / 'design/test.md').exists())
        
        # Check that the manifest file was created
        self.assertTrue((output_dir / 'manifest.yaml').exists())
        
        # Check the manifest content
        with open(output_dir / 'manifest.yaml', 'r') as f:
            manifest = yaml.safe_load(f)
        
        self.assertEqual(manifest['name'], 'test')
        self.assertEqual(manifest['description'], 'Test section')
        self.assertIn('test/file1.py', manifest['files'])
        self.assertIn('test/file2.py', manifest['files'])
        self.assertIn('shared.py', manifest['files'])
        self.assertEqual(manifest['design_files'], ['test.md'])
    
    def test_compile_section_with_missing_files(self):
        """Test compiling a section with missing files."""
        # Update section configuration with a missing file
        config_manager = ConfigManager(self.test_dir)
        section_config = config_manager.read_section_config('test')
        section_config['files'].append('missing.py')
        config_manager.write_section_config('test', section_config)
        
        # Compile the section
        output_dir = self.compiler.compile_section('test')
        
        # Check that existing files were copied
        self.assertTrue((output_dir / 'test/file1.py').exists())
        self.assertTrue((output_dir / 'test/file2.py').exists())
        self.assertTrue((output_dir / 'shared.py').exists())
        
        # Check that the missing file was not copied
        self.assertFalse((output_dir / 'missing.py').exists())
        
        # Check the manifest
        with open(output_dir / 'manifest.yaml', 'r') as f:
            manifest = yaml.safe_load(f)
        
        # Missing file should not be in the manifest
        self.assertNotIn('missing.py', manifest['files'])
    
    def test_compile_all_sections(self):
        """Test compiling all sections."""
        # Create another section
        config_manager = ConfigManager(self.test_dir)
        other_config = {
            'name': 'other',
            'description': 'Other section',
            'files': ['other/file.py', 'shared.py']
        }
        config_manager.write_section_config('other', other_config)
        
        # Create the other section files
        other_dir = self.test_dir / 'other'
        other_dir.mkdir()
        
        with open(self.test_dir / 'other/file.py', 'w') as f:
            f.write('# Other file')
        
        # Create design file
        with open(self.design_dir / 'other.md', 'w') as f:
            f.write('# Design for other section')
        
        # Compile all sections
        compiled = self.compiler.compile_all_sections()
        
        # Check that both sections were compiled
        self.assertEqual(len(compiled), 2)
        self.assertIn('test', compiled)
        self.assertIn('other', compiled)
        
        # Check that both output directories exist
        self.assertTrue(compiled['test'].exists())
        self.assertTrue(compiled['other'].exists())
        
        # Check that files were copied to the right directories
        self.assertTrue((compiled['test'] / 'test/file1.py').exists())
        self.assertTrue((compiled['other'] / 'other/file.py').exists())
        
        # Check that shared file was copied to both directories
        self.assertTrue((compiled['test'] / 'shared.py').exists())
        self.assertTrue((compiled['other'] / 'shared.py').exists())


class TestProjectCompiler(unittest.TestCase):
    """Tests for ProjectCompiler."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Create necessary directories
        config_dir = self.test_dir / '.moduflow/config'
        sections_dir = config_dir / 'sections'
        self.output_dir = self.test_dir / '.compiled_sections'
        self.design_dir = self.test_dir / 'design'
        
        config_dir.mkdir(parents=True)
        sections_dir.mkdir()
        self.output_dir.mkdir()
        self.design_dir.mkdir()
        
        # Create section configurations
        self.section1_config = {
            'name': 'section1',
            'description': 'Section 1',
            'files': ['section1/file1.py', 'section1/file2.py', 'shared.py']
        }
        
        self.section2_config = {
            'name': 'section2',
            'description': 'Section 2',
            'files': ['section2/file.py', 'shared.py']
        }
        
        with open(sections_dir / 'section1.yaml', 'w') as f:
            yaml.dump(self.section1_config, f)
        
        with open(sections_dir / 'section2.yaml', 'w') as f:
            yaml.dump(self.section2_config, f)
        
        # Create test files
        section1_dir = self.test_dir / 'section1'
        section2_dir = self.test_dir / 'section2'
        section1_dir.mkdir()
        section2_dir.mkdir()
        
        with open(self.test_dir / 'section1/file1.py', 'w') as f:
            f.write('# Section 1 file 1')
        
        with open(self.test_dir / 'section1/file2.py', 'w') as f:
            f.write('# Section 1 file 2')
        
        with open(self.test_dir / 'section2/file.py', 'w') as f:
            f.write('# Section 2 file')
        
        with open(self.test_dir / 'shared.py', 'w') as f:
            f.write('# Shared file')
        
        # Create design files
        with open(self.design_dir / 'section1.md', 'w') as f:
            f.write('# Design for section 1')
        
        with open(self.design_dir / 'section2.md', 'w') as f:
            f.write('# Design for section 2')
        
        # Create project compiler
        self.compiler = ProjectCompiler(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_compile_project(self):
        """Test compiling the entire project."""
        # Compile the project
        project_dir = self.compiler.compile_project()
        
        # Check that the project directory was created
        self.assertTrue(project_dir.exists())
        
        # Check that all files were copied
        self.assertTrue((project_dir / 'section1/file1.py').exists())
        self.assertTrue((project_dir / 'section1/file2.py').exists())
        self.assertTrue((project_dir / 'section2/file.py').exists())
        self.assertTrue((project_dir / 'shared.py').exists())
        
        # Check that design files were copied
        self.assertTrue((project_dir / 'design/section1.md').exists())
        self.assertTrue((project_dir / 'design/section2.md').exists())
        
        # Check that the manifest file was created
        self.assertTrue((project_dir / 'manifest.yaml').exists())
        
        # Check the manifest content
        with open(project_dir / 'manifest.yaml', 'r') as f:
            manifest = yaml.safe_load(f)
        
        self.assertEqual(manifest['project_name'], self.test_dir.name)
        self.assertIn('section1', manifest['sections'])
        self.assertIn('section2', manifest['sections'])
        self.assertIn('section1/file1.py', manifest['files'])
        self.assertIn('section1/file2.py', manifest['files'])
        self.assertIn('section2/file.py', manifest['files'])
        self.assertIn('shared.py', manifest['files'])
        self.assertIn('section1.md', manifest['design_files'])
        self.assertIn('section2.md', manifest['design_files'])
    
    def test_compile_project_with_missing_files(self):
        """Test compiling a project with missing files."""
        # Update section configuration with a missing file
        config_manager = ConfigManager(self.test_dir)
        section1_config = config_manager.read_section_config('section1')
        section1_config['files'].append('missing.py')
        config_manager.write_section_config('section1', section1_config)
        
        # Compile the project
        project_dir = self.compiler.compile_project()
        
        # Check that existing files were copied
        self.assertTrue((project_dir / 'section1/file1.py').exists())
        self.assertTrue((project_dir / 'section1/file2.py').exists())
        self.assertTrue((project_dir / 'section2/file.py').exists())
        self.assertTrue((project_dir / 'shared.py').exists())
        
        # Check that the missing file was not copied
        self.assertFalse((project_dir / 'missing.py').exists())
        
        # Check the manifest
        with open(project_dir / 'manifest.yaml', 'r') as f:
            manifest = yaml.safe_load(f)
        
        # Missing file should not be in the manifest files list
        self.assertNotIn('missing.py', manifest['files'])
    
    def test_save_yaml(self):
        """Test the save_yaml method."""
        # Create test data
        test_data = {"key": "value", "nested": {"key": "value"}}
        test_file = self.test_dir / "test.yaml"
        
        # Save YAML
        self.compiler.save_yaml(test_data, test_file)
        
        # Check that the file was created
        self.assertTrue(test_file.exists())
        
        # Check the file content
        with open(test_file, 'r') as f:
            loaded_data = yaml.safe_load(f)
        
        self.assertEqual(loaded_data, test_data)