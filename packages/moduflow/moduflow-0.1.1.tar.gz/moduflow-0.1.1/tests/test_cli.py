"""
Tests for the CLI module.
"""

import os
import shutil
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from moduflow.cli.main import cli


class TestCLI(unittest.TestCase):
    """Tests for CLI commands."""
    
    def setUp(self):
        """Set up test environment."""
        self.runner = CliRunner()
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Set current directory to test directory
        self.old_cwd = os.getcwd()
        os.chdir(self.test_dir)
    
    def tearDown(self):
        """Clean up test environment."""
        os.chdir(self.old_cwd)
        shutil.rmtree(self.test_dir)
    
    def test_cli_without_command(self):
        """Test running the CLI without a command."""
        result = self.runner.invoke(cli)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage:", result.output)
    
    def test_init_command(self):
        """Test the init command."""
        result = self.runner.invoke(cli, ["init"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that directories were created
        self.assertTrue((self.test_dir / ".moduflow").exists())
        self.assertTrue((self.test_dir / ".moduflow/config").exists())
        self.assertTrue((self.test_dir / ".moduflow/config/sections").exists())
        self.assertTrue((self.test_dir / ".compiled_sections").exists())
        self.assertTrue((self.test_dir / "design").exists())
        
        # Check that .gitignore was created
        self.assertTrue((self.test_dir / ".gitignore").exists())
        
        with open(self.test_dir / ".gitignore", "r") as f:
            content = f.read()
        
        self.assertIn(".compiled_sections/", content)
        self.assertIn(".moduflow/", content)
    
    def test_create_section_command(self):
        """Test the create-section command."""
        # Initialize the project first
        self.runner.invoke(cli, ["init"])
        
        # Create a section
        result = self.runner.invoke(
            cli, 
            ["create-section", "test", "--description", "Test section"]
        )
        self.assertEqual(result.exit_code, 0)
        
        # Check that the section configuration was created
        config_path = self.test_dir / ".moduflow/config/sections/test.yaml"
        self.assertTrue(config_path.exists())
        
        # Check that the design file was created
        design_path = self.test_dir / "design/test.md"
        self.assertTrue(design_path.exists())
    
    def test_update_section_command(self):
        """Test the update-section command."""
        # Initialize the project and create a section
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(
            cli, 
            ["create-section", "test", "--description", "Test section"]
        )
        
        # Create a test file
        test_file = self.test_dir / "test.py"
        with open(test_file, "w") as f:
            f.write("# Test file")
        
        # Update the section
        result = self.runner.invoke(
            cli, 
            ["update-section", "test", "--description", "Updated description", "--files", "test.py"]
        )
        self.assertEqual(result.exit_code, 0)
        
        # Check that the section configuration was updated
        import yaml
        config_path = self.test_dir / ".moduflow/config/sections/test.yaml"
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        
        self.assertEqual(config["description"], "Updated description")
        self.assertEqual(config["files"], ["test.py"])
    
    def test_add_files_command(self):
        """Test the add-files command."""
        # Initialize the project and create a section
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(
            cli, 
            ["create-section", "test", "--description", "Test section"]
        )
        
        # Create test files
        test_file1 = self.test_dir / "test1.py"
        test_file2 = self.test_dir / "test2.py"
        with open(test_file1, "w") as f:
            f.write("# Test file 1")
        with open(test_file2, "w") as f:
            f.write("# Test file 2")
        
        # Add files to the section
        result = self.runner.invoke(
            cli, 
            ["add-files", "test", "test1.py", "test2.py"]
        )
        self.assertEqual(result.exit_code, 0)
        
        # Check that the section configuration was updated
        import yaml
        config_path = self.test_dir / ".moduflow/config/sections/test.yaml"
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        
        self.assertIn("test1.py", config["files"])
        self.assertIn("test2.py", config["files"])
    
    def test_add_file_to_sections_command(self):
        """Test the add-file command."""
        # Initialize the project and create sections
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(cli, ["create-section", "section1"])
        self.runner.invoke(cli, ["create-section", "section2"])
        
        # Create a shared file
        shared_file = self.test_dir / "shared.py"
        with open(shared_file, "w") as f:
            f.write("# Shared file")
        
        # Add file to multiple sections
        result = self.runner.invoke(
            cli, 
            ["add-file", "shared.py", "section1,section2"]
        )
        self.assertEqual(result.exit_code, 0)
        
        # Check that both section configurations were updated
        import yaml
        
        with open(self.test_dir / ".moduflow/config/sections/section1.yaml", "r") as f:
            config1 = yaml.safe_load(f)
        
        with open(self.test_dir / ".moduflow/config/sections/section2.yaml", "r") as f:
            config2 = yaml.safe_load(f)
        
        self.assertIn("shared.py", config1["files"])
        self.assertIn("shared.py", config2["files"])
    
    def test_compile_section_command(self):
        """Test the compile-section command."""
        # Initialize the project and create a section
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(cli, ["create-section", "test"])
        
        # Create a test file
        test_dir = self.test_dir / "test"
        test_dir.mkdir()
        test_file = test_dir / "test.py"
        with open(test_file, "w") as f:
            f.write("# Test file")
        
        # Add file to the section
        self.runner.invoke(cli, ["add-files", "test", "test/test.py"])
        
        # Compile the section
        result = self.runner.invoke(cli, ["compile-section", "test"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that the output directory was created
        output_dir = self.test_dir / ".compiled_sections/test"
        self.assertTrue(output_dir.exists())
        
        # Check that the file was copied
        self.assertTrue((output_dir / "test/test.py").exists())
    
    def test_compile_all_command(self):
        """Test the compile-all command."""
        # Initialize the project and create sections
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(cli, ["create-section", "section1"])
        self.runner.invoke(cli, ["create-section", "section2"])
        
        # Create test files
        section1_dir = self.test_dir / "section1"
        section2_dir = self.test_dir / "section2"
        section1_dir.mkdir()
        section2_dir.mkdir()
        
        with open(section1_dir / "file1.py", "w") as f:
            f.write("# Section 1 file")
        
        with open(section2_dir / "file2.py", "w") as f:
            f.write("# Section 2 file")
        
        # Add files to sections
        self.runner.invoke(cli, ["add-files", "section1", "section1/file1.py"])
        self.runner.invoke(cli, ["add-files", "section2", "section2/file2.py"])
        
        # Compile all sections
        result = self.runner.invoke(cli, ["compile-all"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that output directories were created
        self.assertTrue((self.test_dir / ".compiled_sections/section1").exists())
        self.assertTrue((self.test_dir / ".compiled_sections/section2").exists())
        
        # Check that files were copied
        self.assertTrue((self.test_dir / ".compiled_sections/section1/section1/file1.py").exists())
        self.assertTrue((self.test_dir / ".compiled_sections/section2/section2/file2.py").exists())
    
    def test_compile_project_command(self):
        """Test the compile-project command."""
        # Initialize the project and create sections
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(cli, ["create-section", "section1"])
        self.runner.invoke(cli, ["create-section", "section2"])
        
        # Create test files
        section1_dir = self.test_dir / "section1"
        section2_dir = self.test_dir / "section2"
        section1_dir.mkdir()
        section2_dir.mkdir()
        
        with open(section1_dir / "file1.py", "w") as f:
            f.write("# Section 1 file")
        
        with open(section2_dir / "file2.py", "w") as f:
            f.write("# Section 2 file")
        
        with open(self.test_dir / "shared.py", "w") as f:
            f.write("# Shared file")
        
        # Add files to sections
        self.runner.invoke(cli, ["add-files", "section1", "section1/file1.py"])
        self.runner.invoke(cli, ["add-files", "section2", "section2/file2.py"])
        self.runner.invoke(cli, ["add-file", "shared.py", "section1,section2"])
        
        # Compile the project
        result = self.runner.invoke(cli, ["compile-project"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that the project directory was created
        project_dir = self.test_dir / ".compiled_sections/project"
        self.assertTrue(project_dir.exists())
        
        # Check that all files were copied
        self.assertTrue((project_dir / "section1/file1.py").exists())
        self.assertTrue((project_dir / "section2/file2.py").exists())
        self.assertTrue((project_dir / "shared.py").exists())
    
    def test_compile_config_command(self):
        """Test the compile-config command."""
        # Initialize the project and create sections
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(cli, ["create-section", "section1"])
        self.runner.invoke(cli, ["create-section", "section2"])
        
        # Compile the configuration
        result = self.runner.invoke(cli, ["compile-config"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that the compiled configuration was created
        compiled_path = self.test_dir / ".moduflow/config/compiled.yaml"
        self.assertTrue(compiled_path.exists())
        
        # Check the compiled configuration content
        import yaml
        with open(compiled_path, "r") as f:
            compiled = yaml.safe_load(f)
        
        self.assertIn("sections", compiled)
        self.assertIn("section1", compiled["sections"])
        self.assertIn("section2", compiled["sections"])
    
    def test_list_sections_command(self):
        """Test the list command."""
        # Initialize the project and create sections
        self.runner.invoke(cli, ["init"])
        self.runner.invoke(cli, ["create-section", "section1", "--description", "Section 1"])
        self.runner.invoke(cli, ["create-section", "section2", "--description", "Section 2"])
        
        # Add a shared file
        with open(self.test_dir / "shared.py", "w") as f:
            f.write("# Shared file")
        
        self.runner.invoke(cli, ["add-file", "shared.py", "section1,section2"])
        
        # List sections
        result = self.runner.invoke(cli, ["list"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that both sections are listed
        self.assertIn("section1", result.output)
        self.assertIn("section2", result.output)
        self.assertIn("Section 1", result.output)
        self.assertIn("Section 2", result.output)
        
        # Check that the shared file is listed
        self.assertIn("shared.py", result.output)
    
    def test_analyze_project_command(self):
        """Test the analyze command."""
        # Initialize the project
        self.runner.invoke(cli, ["init"])
        
        # Create test directories and files
        users_dir = self.test_dir / "users"
        core_dir = self.test_dir / "core"
        users_dir.mkdir()
        core_dir.mkdir()
        
        with open(users_dir / "__init__.py", "w") as f:
            f.write("# Users module")
        
        with open(users_dir / "models.py", "w") as f:
            f.write("# User models")
        
        with open(core_dir / "__init__.py", "w") as f:
            f.write("# Core module")
        
        with open(core_dir / "settings.py", "w") as f:
            f.write("# Core settings")
        
        # Analyze the project
        result = self.runner.invoke(cli, ["analyze"])
        self.assertEqual(result.exit_code, 0)
        
        # Check that the analysis found the directories
        self.assertIn("users", result.output)
        self.assertIn("core", result.output)
    
    @patch('moduflow.cli.commands.PromptGenerator')
    def test_get_prompt_command_to_stdout(self, mock_generator_class):
        """Test the get-prompt command writing to stdout."""
        # Setup mock
        mock_generator = mock_generator_class.return_value
        mock_generator.generate_prompt.return_value = "Mock prompt content"
        
        # Initialize the project
        self.runner.invoke(cli, ["init"])
        
        # Get the prompt
        result = self.runner.invoke(cli, ["get-prompt"])
        
        # Check that the prompt generator was called
        mock_generator.generate_prompt.assert_called_once()
        
        # Check that the output contains the mock content
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Mock prompt content", result.output)

    @patch('moduflow.cli.commands.PromptGenerator')
    def test_get_prompt_command_to_file(self, mock_generator_class):
        """Test the get-prompt command writing to a file."""
        # Setup mock
        mock_generator = mock_generator_class.return_value
        mock_generator.generate_prompt.return_value = "Mock prompt content"
        
        # Initialize the project
        self.runner.invoke(cli, ["init"])
        
        # Create a temporary file
        output_file = str(self.test_dir / "prompt.md")
        
        # Get the prompt with output to file
        result = self.runner.invoke(cli, ["get-prompt", "--output", output_file])
        
        # Check that the prompt generator was called
        mock_generator.generate_prompt.assert_called_once()
        
        # Check that the file was created
        self.assertTrue(Path(output_file).exists())
        
        # Check the file content
        with open(output_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "Mock prompt content")


if __name__ == "__main__":
    unittest.main()