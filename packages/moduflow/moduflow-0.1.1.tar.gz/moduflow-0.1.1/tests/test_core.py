"""
Tests for core functionality.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest
import yaml

from moduflow.core.config import ConfigManager
from moduflow.core.paths import PathManager


class TestConfigManager(unittest.TestCase):
    """Tests for ConfigManager."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for tests
        self.test_dir = Path(tempfile.mkdtemp())
        self.config_manager = ConfigManager(self.test_dir)
        
        # Create config directories
        self.config_manager.init_config()
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_init_config(self):
        """Test initialization of configuration."""
        # Check that directories were created
        self.assertTrue(self.config_manager.config_dir.exists())
        self.assertTrue(self.config_manager.sections_dir.exists())
        
        # Check that compiled config was created
        self.assertTrue(self.config_manager.compiled_path.exists())
        
        # Check compiled config content
        compiled = self.config_manager.read_compiled_config()
        self.assertEqual(compiled, {'sections': {}})
    
    def test_write_section_config(self):
        """Test writing a section configuration."""
        # Create a section configuration
        section_config = {
            'name': 'test',
            'description': 'Test section',
            'files': ['test.py', 'test2.py']
        }
        
        # Write the configuration
        self.config_manager.write_section_config('test', section_config)
        
        # Check that the file was created
        section_path = self.config_manager.sections_dir / 'test.yaml'
        self.assertTrue(section_path.exists())
        
        # Check the file content
        with open(section_path, 'r') as f:
            content = yaml.safe_load(f)
        
        self.assertEqual(content, section_config)
    
    def test_read_section_config(self):
        """Test reading a section configuration."""
        # Create a section configuration
        section_config = {
            'name': 'test',
            'description': 'Test section',
            'files': ['test.py', 'test2.py']
        }
        
        # Write the configuration
        self.config_manager.write_section_config('test', section_config)
        
        # Read the configuration
        read_config = self.config_manager.read_section_config('test')
        
        # Check the content
        self.assertEqual(read_config, section_config)
    
    def test_read_section_config_not_found(self):
        """Test reading a non-existent section configuration."""
        with self.assertRaises(FileNotFoundError):
            self.config_manager.read_section_config('nonexistent')
    
    def test_read_all_section_configs(self):
        """Test reading all section configurations."""
        # Create two section configurations
        section1_config = {
            'name': 'test1',
            'description': 'Test section 1',
            'files': ['test1.py']
        }
        
        section2_config = {
            'name': 'test2',
            'description': 'Test section 2',
            'files': ['test2.py']
        }
        
        # Write the configurations
        self.config_manager.write_section_config('test1', section1_config)
        self.config_manager.write_section_config('test2', section2_config)
        
        # Read all configurations
        configs = self.config_manager.read_all_section_configs()
        
        # Check the content
        self.assertEqual(len(configs), 2)
        self.assertEqual(configs['test1'], section1_config)
        self.assertEqual(configs['test2'], section2_config)
    
    def test_compile_config(self):
        """Test compiling section configurations."""
        # Create two section configurations
        section1_config = {
            'name': 'test1',
            'description': 'Test section 1',
            'files': ['test1.py']
        }
        
        section2_config = {
            'name': 'test2',
            'description': 'Test section 2',
            'files': ['test2.py']
        }
        
        # Write the configurations
        self.config_manager.write_section_config('test1', section1_config)
        self.config_manager.write_section_config('test2', section2_config)
        
        # Compile the configurations
        compiled = self.config_manager.compile_config()
        
        # Check the compiled configuration
        expected = {
            'sections': {
                'test1': section1_config,
                'test2': section2_config
            }
        }
        self.assertEqual(compiled, expected)
        
        # Check that the compiled file was created
        self.assertTrue(self.config_manager.compiled_path.exists())
        
        # Check the file content
        with open(self.config_manager.compiled_path, 'r') as f:
            content = yaml.safe_load(f)
        
        self.assertEqual(content, expected)
    
    def test_find_files_in_multiple_sections(self):
        """Test finding files used in multiple sections."""
        # Create two section configurations with a shared file
        section1_config = {
            'name': 'test1',
            'description': 'Test section 1',
            'files': ['test1.py', 'shared.py']
        }
        
        section2_config = {
            'name': 'test2',
            'description': 'Test section 2',
            'files': ['test2.py', 'shared.py']
        }
        
        # Write the configurations
        self.config_manager.write_section_config('test1', section1_config)
        self.config_manager.write_section_config('test2', section2_config)
        
        # Find shared files
        shared_files = self.config_manager.find_files_in_multiple_sections()
        
        # Check the result
        self.assertEqual(sorted(shared_files['shared.py']), sorted(['test1', 'test2']))

    
    def test_add_file_to_sections(self):
        """Test adding a file to multiple sections."""
        # Create two section configurations
        section1_config = {
            'name': 'test1',
            'description': 'Test section 1',
            'files': ['test1.py']
        }
        
        section2_config = {
            'name': 'test2',
            'description': 'Test section 2',
            'files': ['test2.py']
        }
        
        # Write the configurations
        self.config_manager.write_section_config('test1', section1_config)
        self.config_manager.write_section_config('test2', section2_config)
        
        # Add a file to both sections
        self.config_manager.add_file_to_sections('shared.py', ['test1', 'test2'])
        
        # Read the updated configurations
        updated1 = self.config_manager.read_section_config('test1')
        updated2 = self.config_manager.read_section_config('test2')
        
        # Check that the file was added
        self.assertIn('shared.py', updated1['files'])
        self.assertIn('shared.py', updated2['files'])


class TestPathManager(unittest.TestCase):
    """Tests for PathManager."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for tests
        self.test_dir = Path(tempfile.mkdtemp())
        self.path_manager = PathManager(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_ensure_directories(self):
        """Test ensuring directories exist."""
        # Ensure directories
        self.path_manager.ensure_directories()
        
        # Check that directories were created
        self.assertTrue(self.path_manager.config_dir.exists())
        self.assertTrue(self.path_manager.sections_dir.exists())
        self.assertTrue(self.path_manager.output_dir.exists())
        self.assertTrue(self.path_manager.design_dir.exists())
    
    def test_get_section_config_path(self):
        """Test getting a section configuration path."""
        # Get the path
        path = self.path_manager.get_section_config_path('test')
        
        # Check the path
        expected = self.path_manager.sections_dir / 'test.yaml'
        self.assertEqual(path, expected)
    
    def test_get_compiled_config_path(self):
        """Test getting the compiled configuration path."""
        # Get the path
        path = self.path_manager.get_compiled_config_path()
        
        # Check the path
        expected = self.path_manager.config_dir / 'compiled.yaml'
        self.assertEqual(path, expected)
    
    def test_get_section_output_dir(self):
        """Test getting a section output directory."""
        # Get the path
        path = self.path_manager.get_section_output_dir('test')
        
        # Check the path
        expected = self.path_manager.output_dir / 'test'
        self.assertEqual(path, expected)
    
    def test_get_project_output_dir(self):
        """Test getting the project output directory."""
        # Get the path
        path = self.path_manager.get_project_output_dir()
        
        # Check the path
        expected = self.path_manager.output_dir / 'project'
        self.assertEqual(path, expected)
    
    def test_get_design_file_path(self):
        """Test getting a design file path."""
        # Get the path
        path = self.path_manager.get_design_file_path('test')
        
        # Check the path
        expected = self.path_manager.design_dir / 'test.md'
        self.assertEqual(path, expected)


if __name__ == '__main__':
    unittest.main()