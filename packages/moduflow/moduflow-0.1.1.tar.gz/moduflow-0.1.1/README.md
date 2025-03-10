# ModuFlow

[![Documentation Status](https://img.shields.io/badge/docs-gh--pages-blue)](https://moduflow.github.io/moduflow/)

A command-line tool for modular development with Test-Driven Development (TDD) support.

## Overview

ModuFlow helps you organize your codebase into logical modules, making it easier to:

- Implement Test-Driven Development (TDD) for each module
- Keep track of which files belong to which module
- Compile modules separately or together
- Generate AI development prompts based on the project structure

## Installation

```bash
pip install moduflow
```

For development:

```bash
git clone https://github.com/moduflow/moduflow.git
cd moduflow
pip install -e .
```

## Core Concepts

- **Modules**: Logical groupings of files that represent a component or feature
- **Module Configuration**: YAML files stored in `.moduflow/config/sections/`
- **Design Files**: Stored in `design/` directory with module-specific design information
- **Compilation**: Files from modules are compiled into `.compiled_sections/` directory

## Usage

### Initialize a project

```bash
moduflow init
```

This creates the necessary directory structure and configuration files.

### Working with modules

```bash
# Create a new module
moduflow create-section users --description "User authentication and management"

# Add files to a module
moduflow add-files users users/auth.py users/models.py

# Add a file to multiple modules
moduflow add-file .env users,core,api
```

### Compiling code

```bash
# Compile a specific module
moduflow compile-section users

# Compile all modules separately
moduflow compile-all

# Compile the entire project
moduflow compile-project
```

### Managing the project

```bash
# List all modules and their files
moduflow list

# Analyze the project structure and suggest modules
moduflow analyze

# Generate AI development prompt
moduflow get-prompt --output ai_prompt.md
```

## Configuration Structure

ModuFlow uses YAML for configuration, with separate files for each module:

```
.moduflow/                 # Hidden directory for configuration files
├── config/                # Configuration directory
│   ├── sections/          # Individual module configurations
│   │   ├── users.yaml     # Users module config
│   │   ├── core.yaml      # Core module config
│   │   └── ...            # Other module configs
│   └── compiled.yaml      # Compiled configuration (generated)
```

Example module YAML file (users.yaml):

```yaml
name: users
description: User authentication, registration, and profile management
files:
  - users/__init__.py
  - users/models.py
  - users/views.py
  - users/tests/test_models.py
  - .env
  - requirements.txt
```

## Development Workflow

1. Initialize your project with `moduflow init`
2. Define your modules using `create-section`
3. Create design files in the `design/` directory for each module
4. Use `get-prompt` to generate an AI development prompt
5. Implement each module using TDD
6. Use `compile-section` to verify that each module works independently
7. Use `compile-project` for final integration

## Documentation
Check out our [documentation](https://moduflow.github.io/moduflow/).

## License

MIT