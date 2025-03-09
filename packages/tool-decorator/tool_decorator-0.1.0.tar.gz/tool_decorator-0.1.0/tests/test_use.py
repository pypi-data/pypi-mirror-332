from datetime import datetime

from anthropic import Anthropic

from tool_decorator import tool


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
    messages=[{"role": "user", "content": "What is the current time?"}],
    tools=[get_time.definition],  # Use definition attribute directly
)

# Print the response to show it worked
print("Response received successfully!")
print(f"Model: {response.model}")

# Print the response content
print("\nResponse content:")
print(response.content)

print("\nAPI call successful with the updated tool definition format!")
