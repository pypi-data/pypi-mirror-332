"""
Tests for the utils module.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch, MagicMock

from moduflow.utils.helpers import (
    normalize_path,
    is_path_within,
    find_project_root,
    list_python_modules,
    camel_to_snake,
    snake_to_camel,
    run_command,
    get_terminal_width
)


class TestHelpers(unittest.TestCase):
    """Tests for helper functions."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Create a test directory structure
        (self.test_dir / ".moduflow").mkdir()
        (self.test_dir / "module1").mkdir()
        (self.test_dir / "module2").mkdir()
        
        # Create test Python modules
        with open(self.test_dir / "module1" / "__init__.py", "w") as f:
            f.write("# Module 1 init")
        
        with open(self.test_dir / "module1" / "file1.py", "w") as f:
            f.write("# Module 1 file 1")
        
        with open(self.test_dir / "module2" / "__init__.py", "w") as f:
            f.write("# Module 2 init")
        
        with open(self.test_dir / "module2" / "file2.py", "w") as f:
            f.write("# Module 2 file 2")
        
        with open(self.test_dir / "standalone.py", "w") as f:
            f.write("# Standalone file")
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_normalize_path(self):
        """Test normalizing a path."""
        # Test with a relative path
        relative_path = "dir1/dir2"
        normalized = normalize_path(relative_path)
        
        # The normalized path should be absolute
        self.assertTrue(os.path.isabs(normalized))
        
        # Test with an absolute path
        abs_path = os.path.abspath("/usr/local/bin")
        normalized = normalize_path(abs_path)
        
        # The normalized path should be the same as the absolute path
        self.assertEqual(normalized, abs_path)
    
    def test_is_path_within(self):
        """Test checking if a path is within another path."""
        # Create test paths
        parent = self.test_dir
        child = parent / "module1"
        sibling = parent / "module2"
        
        # Test a child path
        self.assertTrue(is_path_within(child, parent))
        
        # Test the parent itself
        self.assertTrue(is_path_within(parent, parent))
        
        # Test a sibling (should be False)
        self.assertFalse(is_path_within(sibling, child))
        
        # Test an unrelated path
        unrelated = Path("/tmp/other")
        self.assertFalse(is_path_within(unrelated, parent))
    
    @patch('os.getcwd')
    def test_find_project_root(self, mock_getcwd):
        """Test finding the project root directory."""
        # Mock getcwd to return the test directory
        mock_getcwd.return_value = str(self.test_dir)
        
        # Test finding the project root (.moduflow exists)
        root = find_project_root()
        self.assertEqual(root, self.test_dir)
        
        # Test with a subdirectory
        mock_getcwd.return_value = str(self.test_dir / "module1")
        root = find_project_root()
        self.assertEqual(root, self.test_dir)
        
        # Test with a specific current directory
        root = find_project_root(self.test_dir / "module2")
        self.assertEqual(root, self.test_dir)
        
        # Test with a directory that has no project markers
        temp_dir = Path(tempfile.mkdtemp())
        try:
            with self.assertRaises(FileNotFoundError):
                find_project_root(temp_dir)
        finally:
            shutil.rmtree(temp_dir)
    
    def test_list_python_modules(self):
        """Test listing Python modules in a directory."""
        # List modules in the test directory
        modules = list_python_modules(self.test_dir)
        
        # Should find module1 and module2 (directories with __init__.py)
        self.assertIn("module1", modules)
        self.assertIn("module2", modules)
        
        # Should also find standalone.py (as "standalone")
        self.assertIn("standalone", modules)
        
        # Should not find __init__.py itself
        self.assertNotIn("__init__", modules)
    
    def test_camel_to_snake(self):
        """Test converting camelCase to snake_case."""
        test_cases = [
            ("camelCase", "camel_case"),
            ("PascalCase", "pascal_case"),
            ("HTTPRequest", "http_request"),
            ("simpleWord", "simple_word"),
            ("ABC", "abc"),
            ("ABCWord", "abc_word"),
            ("wordWithNUMBER123", "word_with_number123"),
        ]
        
        for camel, snake in test_cases:
            self.assertEqual(camel_to_snake(camel), snake)
    
    def test_snake_to_camel(self):
        """Test converting snake_case to camelCase."""
        test_cases = [
            ("snake_case", "snakeCase"),
            ("simple_word", "simpleWord"),
            ("http_request", "httpRequest"),
            ("word_with_number_123", "wordWithNumber123"),
            ("single", "single"),
        ]
        
        for snake, camel in test_cases:
            self.assertEqual(snake_to_camel(snake), camel)
    
    @patch('subprocess.Popen')
    def test_run_command(self, mock_popen):
        """Test running a command."""
        # Mock the Popen process
        mock_process = MagicMock()
        mock_process.communicate.return_value = ("stdout output", "stderr output")
        mock_process.returncode = 0
        mock_popen.return_value = mock_process
        
        # Run a test command
        return_code, stdout, stderr = run_command(["echo", "hello"])
        
        # Check that Popen was called with the right arguments
        mock_popen.assert_called_once()
        args, kwargs = mock_popen.call_args
        self.assertEqual(args[0], ["echo", "hello"])
        
        # Check the returned values
        self.assertEqual(return_code, 0)
        self.assertEqual(stdout, "stdout output")
        self.assertEqual(stderr, "stderr output")
        
        # Test with a working directory
        run_command(["ls"], cwd=self.test_dir)
        
        # Check that Popen was called with the right cwd
        args, kwargs = mock_popen.call_args
        self.assertEqual(kwargs["cwd"], self.test_dir)
    
    @patch('shutil.get_terminal_size')
    def test_get_terminal_width(self, mock_get_terminal_size):
        """Test getting the terminal width."""
        # Mock the terminal size
        mock_get_terminal_size.return_value = MagicMock(columns=100)
        
        # Get the terminal width
        width = get_terminal_width()
        
        # Check the returned value
        self.assertEqual(width, 100)
        
        # Test the fallback when get_terminal_size raises an exception
        mock_get_terminal_size.side_effect = Exception("Terminal size not available")
        width = get_terminal_width()
        
        # Should return the default value
        self.assertEqual(width, 80)


if __name__ == "__main__":
    unittest.main()