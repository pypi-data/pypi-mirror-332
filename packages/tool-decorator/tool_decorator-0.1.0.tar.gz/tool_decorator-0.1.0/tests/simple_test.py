import json

from tool_decorator import tool


@tool()
def add(a: int, b: int = 0):
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return a + b


# Access the tool definition directly as an attribute
definition = add.definition

# Print the definition with nice formatting
print(json.dumps(definition, indent=2))
