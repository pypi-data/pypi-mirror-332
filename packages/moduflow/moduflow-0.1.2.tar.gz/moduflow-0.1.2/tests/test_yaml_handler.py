"""
Tests for YamlHandler.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest
import yaml

from moduflow.handlers.yaml_handler import YamlHandler


class TestYamlHandler(unittest.TestCase):
    """Tests for YamlHandler."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.test_file = self.test_dir / "test.yaml"
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_load_yaml(self):
        """Test loading YAML from a file."""
        # Create a YAML file
        test_data = {"key": "value", "list": [1, 2, 3]}
        with open(self.test_file, "w") as f:
            yaml.dump(test_data, f)
        
        # Load the YAML file
        loaded_data = YamlHandler.load_yaml(self.test_file)
        
        # Check the loaded data
        self.assertEqual(loaded_data, test_data)
    
    def test_load_yaml_file_not_found(self):
        """Test loading YAML from a non-existent file."""
        # Try to load a non-existent file
        with self.assertRaises(FileNotFoundError):
            YamlHandler.load_yaml(self.test_dir / "non_existent.yaml")
    
    def test_load_yaml_invalid_yaml(self):
        """Test loading invalid YAML."""
        # Create an invalid YAML file
        with open(self.test_file, "w") as f:
            f.write("invalid: yaml: content: with: too: many: colons")
        
        # Try to load the invalid YAML file
        with self.assertRaises(yaml.YAMLError):
            YamlHandler.load_yaml(self.test_file)
    
    def test_save_yaml(self):
        """Test saving YAML to a file."""
        # Create test data
        test_data = {"key": "value", "list": [1, 2, 3]}
        
        # Save the data to a YAML file
        YamlHandler.save_yaml(test_data, self.test_file)
        
        # Check that the file was created
        self.assertTrue(self.test_file.exists())
        
        # Load the file and check the content
        with open(self.test_file, "r") as f:
            loaded_data = yaml.safe_load(f)
        
        self.assertEqual(loaded_data, test_data)
    
    def test_merge_yaml(self):
        """Test merging YAML data."""
        # Create base and override data
        base = {"key1": "value1", "key2": "value2", "nested": {"subkey1": "subvalue1"}}
        override = {"key2": "new_value2", "key3": "value3", "nested": {"subkey2": "subvalue2"}}
        
        # Merge the data
        merged = YamlHandler.merge_yaml(base, override)
        
        # Check the merged data
        self.assertEqual(merged["key1"], "value1")  # From base
        self.assertEqual(merged["key2"], "new_value2")  # From override
        self.assertEqual(merged["key3"], "value3")  # From override
        self.assertEqual(merged["nested"]["subkey1"], "subvalue1")  # From base
        self.assertEqual(merged["nested"]["subkey2"], "subvalue2")  # From override
    
    def test_yaml_to_string(self):
        """Test converting YAML data to a string."""
        # Create test data
        test_data = {"key": "value", "list": [1, 2, 3]}
        
        # Convert to string
        yaml_str = YamlHandler.yaml_to_string(test_data)
        
        # Check that the string is valid YAML
        self.assertIsInstance(yaml_str, str)
        loaded_data = yaml.safe_load(yaml_str)
        self.assertEqual(loaded_data, test_data)
    
    def test_string_to_yaml(self):
        """Test converting a string to YAML data."""
        # Create a YAML string
        yaml_str = "key: value\nlist:\n- 1\n- 2\n- 3\n"
        
        # Convert to YAML data
        data = YamlHandler.string_to_yaml(yaml_str)
        
        # Check the data
        self.assertEqual(data["key"], "value")
        self.assertEqual(data["list"], [1, 2, 3])
    
    def test_string_to_yaml_invalid(self):
        """Test converting an invalid string to YAML data."""
        # Create an invalid YAML string
        yaml_str = "invalid: yaml: with: too: many: colons"
        
        # Try to convert to YAML data
        with self.assertRaises(yaml.YAMLError):
            YamlHandler.string_to_yaml(yaml_str)