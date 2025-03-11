"""
Command-line interface for ModuFlow.

This module provides the entry point for the ModuFlow CLI using Click.
"""

import click
import sys
import os
from pathlib import Path

from moduflow.cli.commands import (
    init_command,
    create_section_command,
    update_section_command,
    add_files_command,
    add_file_to_sections_command,
    compile_section_command,
    compile_all_command,
    compile_project_command,
    compile_config_command,
    list_sections_command,
    analyze_project_command,
    get_prompt_command,
)


@click.group()
@click.version_option()
def cli():
    """ModuFlow - Section-based development with Test-Driven Development support.
    
    This tool helps organize your code into logical sections,
    making it easier to implement Test-Driven Development.
    """
    pass


# Register commands
cli.add_command(init_command)
cli.add_command(create_section_command)
cli.add_command(update_section_command)
cli.add_command(add_files_command)
cli.add_command(add_file_to_sections_command)
cli.add_command(compile_section_command)
cli.add_command(compile_all_command)
cli.add_command(compile_project_command)
cli.add_command(compile_config_command)
cli.add_command(list_sections_command)
cli.add_command(analyze_project_command)
cli.add_command(get_prompt_command)


# Allow running this file directly for development purposes
if __name__ == "__main__":
    cli()