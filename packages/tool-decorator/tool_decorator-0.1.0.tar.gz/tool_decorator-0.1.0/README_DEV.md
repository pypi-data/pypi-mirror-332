# Tool Decorator Development Guide

This document contains information for developers contributing to the tool_decorator project.

## Building with Hatch

This project uses [Hatch](https://hatch.pypa.io/) for building, testing, and managing development environments.

### Installing Hatch

```bash
pip install hatch
```

### Common Commands

```bash
# Run tests
hatch run test

# Run linting and type checking
hatch run lint:all

# Format code
hatch run lint:fmt

# Build the package
hatch build
```

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. To set up the pre-commit hooks:

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```

2. Install the git hooks:
   ```bash
   pre-commit install
   ```

The pre-commit configuration includes:
- Code formatting with Black
- Linting with Ruff
- Type checking with MyPy
- Various file checks (YAML, TOML, trailing whitespace, etc.)
