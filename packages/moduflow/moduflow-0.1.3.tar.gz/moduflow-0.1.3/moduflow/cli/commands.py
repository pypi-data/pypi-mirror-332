"""
Command implementations for the ModuFlow CLI.

This module contains the implementations of the CLI commands.
"""

import os
import sys
import click
from pathlib import Path
from typing import List, Optional

from moduflow.handlers.section_handler import SectionHandler
from moduflow.prompts.templates import PromptGenerator
from moduflow.core.config import ConfigManager


@click.command("init")
def init_command():
    """Initialize a new section-based project."""
    handler = SectionHandler()
    handler.init_project()


@click.command("create-section")
@click.argument("name")
@click.option("--description", "-d", default="", help="Description of the section")
@click.option("--files", "-f", multiple=True, help="Initial files to include in the section")
def create_section_command(name: str, description: str, files: List[str]):
    """Create a new section."""
    handler = SectionHandler()
    handler.create_section(name, description, list(files) if files else None)


@click.command("update-section")
@click.argument("name")
@click.option("--description", "-d", help="New description of the section")
@click.option("--files", "-f", multiple=True, help="New list of files for the section")
def update_section_command(name: str, description: Optional[str], files: Optional[List[str]]):
    """Update an existing section."""
    handler = SectionHandler()
    handler.update_section(name, description, list(files) if files else None)


@click.command("add-files")
@click.argument("name")
@click.argument("files", nargs=-1, required=True)
def add_files_command(name: str, files: List[str]):
    """Add files to a section."""
    handler = SectionHandler()
    handler.add_files_to_section(name, list(files))


@click.command("add-file")
@click.argument("file")
@click.argument("sections")
def add_file_to_sections_command(file: str, sections: str):
    """Add a file to multiple sections."""
    section_list = [s.strip() for s in sections.split(",")]
    config_manager = ConfigManager()
    config_manager.add_file_to_sections(file, section_list)
    click.echo(f"Added file '{file}' to sections: {sections}")


@click.command("compile-section")
@click.argument("name")
def compile_section_command(name: str):
    """Compile a section to the output directory."""
    handler = SectionHandler()
    handler.compile_section(name)


@click.command("compile-all")
def compile_all_command():
    """Compile all sections to separate directories."""
    handler = SectionHandler()
    handler.compile_all_sections()


@click.command("compile-project")
def compile_project_command():
    """Compile the entire project to a single directory."""
    handler = SectionHandler()
    handler.compile_project()


@click.command("compile-config")
def compile_config_command():
    """Compile section YAML files into a single configuration."""
    config_manager = ConfigManager()
    compiled = config_manager.compile_config()
    click.echo(f"Configuration compiled to {config_manager.compiled_path}")


@click.command("list")
def list_sections_command():
    """List all sections with their files."""
    handler = SectionHandler()
    handler.list_sections()


@click.command("analyze")
def analyze_project_command():
    """Analyze the project structure and suggest sections."""
    handler = SectionHandler()
    handler.analyze_project()


@click.command("get-prompt")
@click.option("--output", "-o", help="Output file (defaults to stdout)")
def get_prompt_command(output: Optional[str]):
    """Get the AI development prompt."""
    generator = PromptGenerator()
    prompt = generator.generate_prompt()
    
    
    if output:
        with open(output, 'w') as f:
            f.write(prompt)
        click.echo(f"Prompt written to {output}")
    else:
        click.echo(prompt)