"""
Extended tests for the utils module.
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


class TestHelpersEdgeCases(unittest.TestCase):
    """Tests for edge cases in helper functions."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Create a test directory structure
        (self.test_dir / ".git").mkdir()
        (self.test_dir / "module1").mkdir()
        
        # Set current directory to test directory
        self.old_cwd = os.getcwd()
        os.chdir(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        os.chdir(self.old_cwd)
        shutil.rmtree(self.test_dir)
    
    def test_normalize_path_edge_cases(self):
        """Test edge cases for normalize_path."""
        # Test with an empty string
        normalized = normalize_path("")
        self.assertTrue(os.path.isabs(normalized))
        
        # Test with a path containing special characters
        special_path = "dir with spaces/file-with-dashes.txt"
        normalized = normalize_path(special_path)
        self.assertTrue(os.path.isabs(normalized))
        
        # Test with a path containing parent directory references
        parent_path = "../parent/file.txt"
        normalized = normalize_path(parent_path)
        self.assertTrue(os.path.isabs(normalized))
    
    def test_is_path_within_edge_cases(self):
        """Test edge cases for is_path_within."""
        # Test with identical paths
        path = Path("/some/path")
        self.assertTrue(is_path_within(path, path))
        
        # Test with parent path being a file (should be False)
        parent = self.test_dir / "file.txt"
        with open(parent, "w") as f:
            f.write("content")
        child = self.test_dir / "file.txt" / "child"
        self.assertFalse(is_path_within(child, parent))
        
        # Test with paths on different drives (Windows-specific)
        if os.name == "nt":  # Only run on Windows
            c_drive_path = Path("C:/path")
            d_drive_path = Path("D:/path")
            self.assertFalse(is_path_within(d_drive_path, c_drive_path))
    
    def test_find_project_root_with_git(self):
        """Test finding project root with .git directory."""
        # Create a nested directory structure with .git at the root
        nested_dir = self.test_dir / "dir1" / "dir2" / "dir3"
        nested_dir.mkdir(parents=True)
        
        # Change to the nested directory
        os.chdir(nested_dir)
        
        # Find the project root
        root = find_project_root()
        
        # Should find the test_dir (where .git is)
        self.assertEqual(root, self.test_dir)
    
    @patch("os.getcwd")
    def test_find_project_root_at_filesystem_root(self, mock_getcwd):
        """Test finding project root when already at filesystem root."""
        # Mock getcwd to return the filesystem root
        mock_getcwd.return_value = os.path.abspath("/")
        
        # Should raise FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            find_project_root()
    
    def test_list_python_modules_empty_dir(self):
        """Test listing Python modules in an empty directory."""
        # Create an empty directory
        empty_dir = self.test_dir / "empty"
        empty_dir.mkdir()
        
        # List modules
        modules = list_python_modules(empty_dir)
        
        # Should be an empty list
        self.assertEqual(modules, [])
    
    def test_list_python_modules_non_python_files(self):
        """Test listing Python modules with non-Python files."""
        # Create a directory with non-Python files
        dir_path = self.test_dir / "non_python"
        dir_path.mkdir()
        
        # Create some non-Python files
        with open(dir_path / "file.txt", "w") as f:
            f.write("text file")
        
        with open(dir_path / "file.md", "w") as f:
            f.write("markdown file")
        
        # List modules
        modules = list_python_modules(dir_path)
        
        # Should be an empty list
        self.assertEqual(modules, [])
    
    def test_camel_to_snake_edge_cases(self):
        """Test edge cases for camel_to_snake."""
        # Test with an empty string
        self.assertEqual(camel_to_snake(""), "")
        
        # Test with a single lowercase letter
        self.assertEqual(camel_to_snake("a"), "a")
        
        # Test with a single uppercase letter
        self.assertEqual(camel_to_snake("A"), "a")
        
        # Test with all uppercase
        self.assertEqual(camel_to_snake("ABC"), "abc")
        
        # Test with numbers
        self.assertEqual(camel_to_snake("camel123Case"), "camel123_case")
        
        # Test with already snake_case
        self.assertEqual(camel_to_snake("snake_case"), "snake_case")
    
    def test_snake_to_camel_edge_cases(self):
        """Test edge cases for snake_to_camel."""
        # Test with an empty string
        self.assertEqual(snake_to_camel(""), "")
        
        # Test with a single letter
        self.assertEqual(snake_to_camel("a"), "a")
        
        # Test with no underscores
        self.assertEqual(snake_to_camel("word"), "word")
        
        # Test with leading underscore
        self.assertEqual(snake_to_camel("_private"), "_private")
        
        # Test with double underscores
        self.assertEqual(snake_to_camel("snake__case"), "snake_Case")
        
        # Test with trailing underscore
        self.assertEqual(snake_to_camel("snake_"), "snake_")
    
    @patch("subprocess.Popen")
    def test_run_command_with_errors(self, mock_popen):
        """Test run_command with errors."""
        # Mock the Popen process to return an error
        mock_process = MagicMock()
        mock_process.communicate.return_value = ("", "command not found")
        mock_process.returncode = 127
        mock_popen.return_value = mock_process
        
        # Run a command
        return_code, stdout, stderr = run_command(["nonexistent_command"])
        
        # Check the returned values
        self.assertEqual(return_code, 127)
        self.assertEqual(stdout, "")
        self.assertEqual(stderr, "command not found")
    
    @patch("shutil.get_terminal_size")
    def test_get_terminal_width_fallback(self, mock_get_terminal_size):
        """Test the fallback behavior of get_terminal_width."""
        # Mock get_terminal_size to raise an exception
        mock_get_terminal_size.side_effect = OSError("Terminal size not available")
        
        # Get the terminal width
        width = get_terminal_width()
        
        # Should return the default value
        self.assertEqual(width, 80)


if __name__ == "__main__":
    unittest.main()