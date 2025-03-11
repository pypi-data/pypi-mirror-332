#!/usr/bin/env python
from setuptools import setup, find_packages

# This file is kept for compatibility with older pip versions
# Most of the configuration is now in pyproject.toml and setup.cfg

if __name__ == "__main__":
    setup(
        packages=find_packages(),
        # Other setup parameters are in pyproject.toml and setup.cfg
    )