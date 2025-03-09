from datetime import datetime

from anthropic import Anthropic


# Define the get_time function without decorator
def get_time(timezone: str = "UTC"):
    """
    Get the current time.

    Args:
        timezone: The timezone to get the time for (default: UTC)
    """
    # Simple implementation that ignores timezone for demo purposes
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time, "timezone": timezone}


# Manually define the tool definition
get_time_definition = {
    "name": "get_time",
    "description": "Get the current time.",
    "input_schema": {
        "type": "object",
        "properties": {
            "timezone": {
                "type": "string",
                "description": "The timezone to get the time for (default: UTC)",
                "default": "UTC",
            }
        },
        "required": [],
    },
}

# Create a client
client = Anthropic()

# Use the manual tool definition with the SDK
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    messages=[{"role": "user", "content": "What is the current time?"}],
    tools=[get_time_definition],  # Use manually defined tool definition
)

# Print the response to show it worked
print("Response received successfully!")
print(f"Model: {response.model}")

# Print the response content
print("\nResponse content:")
print(response.content)

print("\nAPI call successful with manually defined tool definition!")
