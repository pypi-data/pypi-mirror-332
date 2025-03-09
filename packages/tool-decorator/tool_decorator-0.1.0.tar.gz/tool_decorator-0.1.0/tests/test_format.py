import json

from tool_decorator import tool


@tool()
def get_weather(location: str, unit: str = "celsius"):
    """
    Get the current weather for a location.

    Args:
        location: City name or geographic coordinates
        unit: Temperature unit (celsius or fahrenheit)
    """
    # Actual implementation here
    return {"temperature": 22.5, "conditions": "Sunny"}


# Print the tool definition in a pretty format
print(json.dumps(get_weather.definition, indent=2))
