# Tool Decorator for Anthropic SDK

A Python decorator that simplifies the creation of tool definitions for the Anthropic SDK.

## Overview

This package provides a `@tool` decorator that automatically generates Anthropic-compatible tool definitions from Python functions. It extracts parameter types, descriptions, and other metadata directly from function signatures and docstrings.

## Installation

```bash
pip install tool-decorator
```

## Usage

### Basic Usage

```python
from tool_decorator import tool

@tool(description="Search for information on the web")
def search_web(query: str, max_results: int = 10):
    """
    Performs a web search and returns results.

    Args:
        query: The search query string
        max_results: Maximum number of results to return
    """
    # Implementation here
    pass

# Access the tool definition
tool_definition = search_web.definition
```

### Using with Anthropic SDK

```python
from tool_decorator import tool
from anthropic import Anthropic
from datetime import datetime

# Define a simple tool with the decorator
@tool()
def get_time(timezone: str = "UTC"):
    """
    Get the current time.

    Args:
        timezone: The timezone to get the time for (default: UTC)
    """
    # Simple implementation that ignores timezone for demo purposes
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time, "timezone": timezone}

# Create a client
client = Anthropic()

# Use the tool definition with the SDK
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "What is the current time?"}
    ],
    tools=[
        get_time.definition  # Use definition attribute directly
    ]
)

# Print the response
print("Response received successfully!")
print(f"Model: {response.model}")
print("\nResponse content:")
print(response.content)
```

### Comparison with Manual Definition

Without the decorator, you would need to manually define the tool definition:

```python
# Manual tool definition
get_time_definition = {
    "name": "get_time",
    "description": "Get the current time.",
    "input_schema": {
        "type": "object",
        "properties": {
            "timezone": {
                "type": "string",
                "description": "The timezone to get the time for (default: UTC)",
                "default": "UTC"
            }
        },
        "required": []
    }
}

# Use with Anthropic SDK
tools=[get_time_definition]
```

The decorator approach automatically generates this definition from your function signature and docstring, keeping everything in sync and reducing boilerplate code.

## Generated Tool Definition Format

The decorator generates tool definitions in the required schema format for the Anthropic API.

## Features

- Automatically converts Python type hints to JSON Schema types
- Extracts parameter descriptions from docstrings
- Supports optional parameters with default values
- Generates Anthropic-compatible tool definitions with the required `input_schema` field
- Validates parameter documentation in strict mode

## Development

For information on development, building, and contributing to this project, see [README_DEV.md](README_DEV.md).

## Requirements

- Python 3.8+

## License

MIT License - See LICENSE file for details
