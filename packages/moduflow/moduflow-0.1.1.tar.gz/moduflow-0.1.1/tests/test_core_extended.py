"""
Extended tests for the core module.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest

from moduflow.core.config import ConfigManager
from moduflow.core.paths import PathManager
from moduflow.core.exceptions import ModuFlowError, ConfigError, SectionError, SectionNotFoundError


class TestExceptions(unittest.TestCase):
    """Tests for exception classes."""
    
    def test_moduflow_error(self):
        """Test ModuFlowError."""
        error = ModuFlowError("Test error")
        self.assertEqual(str(error), "Test error")
    
    def test_config_error(self):
        """Test ConfigError."""
        error = ConfigError("Config error")
        self.assertEqual(str(error), "Config error")
        self.assertIsInstance(error, ModuFlowError)
    
    def test_section_error(self):
        """Test SectionError."""
        error = SectionError("Section error")
        self.assertEqual(str(error), "Section error")
        self.assertIsInstance(error, ModuFlowError)
    
    def test_section_not_found_error(self):
        """Test SectionNotFoundError."""
        error = SectionNotFoundError("Section not found")
        self.assertEqual(str(error), "Section not found")
        self.assertIsInstance(error, SectionError)


class TestPathManager(unittest.TestCase):
    """Extended tests for PathManager."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for tests
        self.test_dir = Path(tempfile.mkdtemp())
        self.path_manager = PathManager(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_get_file_paths_by_pattern(self):
        """Test getting file paths by pattern."""
        # Create test files
        (self.test_dir / "file1.txt").touch()
        (self.test_dir / "file2.txt").touch()
        (self.test_dir / "file3.md").touch()
        
        # Test getting all files
        file_paths = self.path_manager.get_file_paths_by_pattern("*.*")
        self.assertEqual(len(file_paths), 3)
        
        # Test getting files by extension
        txt_paths = self.path_manager.get_file_paths_by_pattern("*.txt")
        self.assertEqual(len(txt_paths), 2)
        
        md_paths = self.path_manager.get_file_paths_by_pattern("*.md")
        self.assertEqual(len(md_paths), 1)
    
    def test_get_relative_path(self):
        """Test getting a path relative to the project root."""
        # Create a nested directory structure
        nested_dir = self.test_dir / "dir1" / "dir2"
        nested_dir.mkdir(parents=True)
        
        # Create a file in the nested directory
        test_file = nested_dir / "test_file.txt"
        test_file.touch()
        
        # Get the relative path
        rel_path = self.path_manager.get_relative_path(test_file)
        
        # Check the relative path
        self.assertEqual(rel_path, "dir1/dir2/test_file.txt")


class TestConfigManagerExtended(unittest.TestCase):
    """Extended tests for ConfigManager."""
    
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
    
    def test_config_io_edge_cases(self):
        """Test edge cases for config I/O."""
        # Test reading an empty section configuration
        empty_section_path = self.config_manager.sections_dir / "empty.yaml"
        with open(empty_section_path, 'w') as f:
            f.write("")  # Empty file
        
        # Reading an empty file should return an empty dict
        config = self.config_manager.read_section_config("empty")
        self.assertEqual(config, {})
        
        # Test writing and reading a complex configuration
        complex_config = {
            "name": "complex",
            "description": "Complex section",
            "files": ["file1.py", "file2.py"],
            "nested": {
                "key1": "value1",
                "key2": ["item1", "item2"],
                "key3": {
                    "subkey1": "subvalue1"
                }
            },
            "list_of_dicts": [
                {"name": "item1", "value": 1},
                {"name": "item2", "value": 2}
            ]
        }
        
        self.config_manager.write_section_config("complex", complex_config)
        read_config = self.config_manager.read_section_config("complex")
        
        # Check that complex structures are preserved
        self.assertEqual(read_config, complex_config)
    
    def test_empty_compiled_config(self):
        """Test handling an empty compiled configuration."""
        # Create an empty compiled config
        with open(self.config_manager.compiled_path, 'w') as f:
            f.write("")
        
        # Reading an empty file should return a default structure
        compiled = self.config_manager.read_compiled_config()
        self.assertEqual(compiled, {'sections': {}})
    
    def test_find_files_with_no_sections(self):
        """Test finding files in multiple sections when no sections exist."""
        # No sections have been created yet
        shared_files = self.config_manager.find_files_in_multiple_sections()
        self.assertEqual(shared_files, {})
    
    def test_add_file_to_nonexistent_section(self):
        """Test adding a file to a nonexistent section."""
        # Add a file to a nonexistent section
        self.config_manager.add_file_to_sections("file.py", ["nonexistent"])
        
        # Should not create the nonexistent section
        with self.assertRaises(FileNotFoundError):
            self.config_manager.read_section_config("nonexistent")


if __name__ == "__main__":
    unittest.main()