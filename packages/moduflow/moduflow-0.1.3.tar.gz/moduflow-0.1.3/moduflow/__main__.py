"""
Entry point for running ModuFlow as a module.

This allows running the package directly with:
python -m moduflow
"""

from moduflow.cli.main import cli

if __name__ == "__main__":
    cli()