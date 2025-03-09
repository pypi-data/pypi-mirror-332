import functools
import inspect
from typing import (
    Any,
    Dict,
    Optional,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)


def tool(
    name: Optional[str] = None, description: Optional[str] = None, strict: bool = True
):
    """
    Decorator that adds a .definition property to a function that returns
    a dictionary matching the Anthropic tool definition format.

    Args:
        name: Optional custom name for the tool. If not provided, uses the function name.
        description: Optional description of the tool. If not provided, uses the function docstring.
        strict: If True, raises an error when parameters lack descriptions in the docstring.

    Returns:
        The decorated function with an added .definition property.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        def get_definition() -> Dict[str, Any]:
            """Returns the function's definition as an Anthropic tool definition dictionary."""
            func_name = name or func.__name__
            func_description = (
                description or inspect.getdoc(func) or f"Function {func_name}"
            )

            # Get type annotations and default values
            type_hints = get_type_hints(func)
            signature = inspect.signature(func)
            parameters = signature.parameters

            # Build the properties dict for parameters
            properties = {}
            required = []

            for param_name, param in parameters.items():
                # Skip self/cls for methods
                if (
                    param_name in ("self", "cls")
                    and param.kind == param.POSITIONAL_OR_KEYWORD
                ):
                    continue

                param_type = type_hints.get(param_name, Any)
                param_default = param.default

                # Check if parameter is required
                if param_default is param.empty:
                    required.append(param_name)

                # Extract parameter description from docstring if available
                param_description = ""
                if func.__doc__:
                    for line in func.__doc__.split("\n"):
                        line = line.strip()
                        if line.startswith(f"{param_name}:"):
                            param_description = line[len(param_name) + 1 :].strip()
                        elif line.startswith(
                            f"    {param_name}:"
                        ):  # Handle indented docstring
                            param_description = line[len(param_name) + 5 :].strip()

                # In strict mode, validate that all parameters have descriptions
                if (
                    strict
                    and not param_description
                    and param_name not in ("self", "cls")
                ):
                    raise ValueError(
                        f"Parameter '{param_name}' in function '{func.__name__}' has no description in docstring. "
                        f"Add a description in the format '{param_name}: Description' to the docstring or set strict=False."
                    )

                # Create parameter definition
                param_def = {
                    "type": python_type_to_json_schema(param_type),
                    "description": param_description or f"Parameter {param_name}",
                }

                # Add default value if present
                if param_default is not param.empty and param_default is not None:
                    param_def["default"] = param_default

                properties[param_name] = param_def

            # Build the complete definition with input_schema instead of parameters
            definition = {
                "name": func_name,
                "description": func_description,
                "input_schema": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            }

            return definition

        # Calculate the definition once and store it as an attribute
        wrapper.definition = get_definition()

        return wrapper

    return decorator


def python_type_to_json_schema(py_type: Any) -> str:
    """
    Convert Python type hints to JSON Schema types.

    Args:
        py_type: A Python type hint

    Returns:
        The corresponding JSON Schema type as a string
    """
    # Handle Union types (Optional is Union[T, None])
    origin = get_origin(py_type)
    if origin is Union:
        args = get_args(py_type)
        # Handle Optional[T] specially (Union[T, None])
        if type(None) in args:
            non_none_args = [arg for arg in args if arg is not type(None)]
            if len(non_none_args) == 1:
                return python_type_to_json_schema(non_none_args[0])
        return "string"  # Default to string for complex unions

    # Handle container types
    if origin is list:
        return "array"
    if origin is dict:
        return "object"

    # Handle primitive types
    type_map = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean",
        dict: "object",
        list: "array",
        None: "null",
    }

    return type_map.get(py_type, "string")  # Default to string for unknown types
