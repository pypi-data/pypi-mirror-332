"""
Exceptions for ModuFlow.

This module provides custom exceptions for ModuFlow.
"""


class ModuFlowError(Exception):
    """Base exception for all ModuFlow errors."""
    pass


class ConfigError(ModuFlowError):
    """Error in configuration."""
    pass


class SectionError(ModuFlowError):
    """Error related to sections."""
    pass


class SectionNotFoundError(SectionError):
    """Section not found."""
    pass


class CompilationError(ModuFlowError):
    """Error during compilation."""
    pass


class FileError(ModuFlowError):
    """Error related to files."""
    pass