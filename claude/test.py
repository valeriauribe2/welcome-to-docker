import os

# Load the API key from an environment variable
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Print the API key (for debugging purposes)
print("API Key:", ANTHROPIC_API_KEY)


#print(os.environ.get("ANTHROPIC_API_KEY"))
