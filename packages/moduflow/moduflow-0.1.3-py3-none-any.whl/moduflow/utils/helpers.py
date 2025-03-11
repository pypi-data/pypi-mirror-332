"""
Helper functions for ModuFlow.

This module provides utility functions for ModuFlow.
"""

import os
import re
import platform
import subprocess
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple


def normalize_path(path: str) -> str:
    """Normalize a path for the current platform.
    
    Args:
        path: Path to normalize.
        
    Returns:
        Normalized path.
    """
    return str(Path(path).resolve())


def is_path_within(child_path: Path, parent_path: Path) -> bool:
    """Check if a path is within another path.
    
    Args:
        child_path: Child path to check.
        parent_path: Parent path to check against.
        
    Returns:
        True if child_path is within parent_path, False otherwise.
    """
    # First check if parent_path exists and is a directory
    # If it's a file, a child path cannot be within it
    if parent_path.exists() and not parent_path.is_dir():
        return False
        
    # Handle case of identical paths
    if child_path == parent_path:
        return True
        
    # On Windows, check if the paths are on different drives
    if os.name == "nt" and child_path.drive != parent_path.drive:
        return False
        
    # Try to get the relative path
    try:
        child_path.relative_to(parent_path)
        return True
    except ValueError:
        return False


def find_project_root(current_dir: Optional[str] = None) -> Path:
    """Find the project root directory.
    
    This looks for a .moduflow directory or a git repository.
    
    Args:
        current_dir: Directory to start from. If None, uses current directory.
        
    Returns:
        Path to the project root.
        
    Raises:
        FileNotFoundError: If project root cannot be found.
    """
    search_dir = Path(current_dir or os.getcwd()).resolve()
    
    # Look for .moduflow directory, .git directory, or pyproject.toml
    markers = ['.moduflow', '.git', 'pyproject.toml']
    
    while search_dir != search_dir.parent:
        for marker in markers:
            if (search_dir / marker).exists():
                return search_dir
        
        # Move up one level
        search_dir = search_dir.parent
    
    # If we get here, we couldn't find a project root
    raise FileNotFoundError("Could not find project root. Initialize a project with 'moduflow init'.")


def list_python_modules(directory: Path) -> List[str]:
    """List Python modules in a directory.
    
    Args:
        directory: Directory to search in.
        
    Returns:
        List of module names.
    """
    modules = []
    
    for item in directory.iterdir():
        if item.is_file() and item.suffix == '.py' and item.stem != '__init__':
            modules.append(item.stem)
        elif item.is_dir() and (item / '__init__.py').exists():
            modules.append(item.name)
    
    return modules


def camel_to_snake(name: str) -> str:
    """Convert a camelCase or PascalCase name to snake_case.
    
    Args:
        name: Name to convert.
        
    Returns:
        snake_case name.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(name: str) -> str:
    """Convert a snake_case name to camelCase.
    
    Args:
        name: Name to convert.
        
    Returns:
        camelCase name.
    """
    # Handle empty string
    if not name:
        return ""
        
    # Check for leading underscore to preserve it
    leading_underscore = ""
    if name.startswith("_"):
        # Count leading underscores
        i = 0
        while i < len(name) and name[i] == "_":
            i += 1
        leading_underscore = name[:i]
        name = name[i:]
        
    # Handle trailing underscore
    trailing_underscore = ""
    if name.endswith("_"):
        # Count trailing underscores
        i = len(name) - 1
        while i >= 0 and name[i] == "_":
            i -= 1
        trailing_underscore = name[i+1:]
        name = name[:i+1]
    
    # If string is now empty, return the combined underscores
    if not name:
        return leading_underscore + trailing_underscore
        
    # Split by underscore and convert to camelCase
    components = name.split('_')
    # Handle empty components (which come from double underscores)
    result = components[0]
    
    for i in range(1, len(components)):
        if components[i] == "":
            # Add an underscore for each empty component (which was a double underscore)
            result += "_"
        else:
            result += components[i].title()
    
    # Combine with preserved leading/trailing underscores
    return leading_underscore + result + trailing_underscore


def run_command(cmd: List[str], cwd: Optional[Path] = None) -> Tuple[int, str, str]:
    """Run a command and return its output.
    
    Args:
        cmd: Command to run as a list of strings.
        cwd: Working directory. If None, uses current directory.
        
    Returns:
        Tuple of (return_code, stdout, stderr)
    """
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        universal_newlines=True
    )
    
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr


def get_terminal_width() -> int:
    """Get the width of the terminal.
    
    Returns:
        Width of the terminal in characters.
    """
    try:
        import shutil
        return shutil.get_terminal_size().columns
    except:
        return 80  # Default fallback