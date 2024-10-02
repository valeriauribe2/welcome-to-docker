import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

# Load API key
api_key = os.environ.get("ANTHROPIC_API_KEY")
print(f"API Key: {api_key}")  # Verify that the API key is loaded

client = Anthropic(api_key=api_key)

try:
    # Create and send a message to Claude 3.5 Sonnet
    message = client.messages.create(
        model="claude-3.5-sonnet",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude"},
        ],
    )
    print(message.content)

except Exception as e:
    print(f"An error occurred: {e}")