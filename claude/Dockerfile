# Start with a base Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install pip if it's not included
RUN apt-get update && apt-get install -y python3-pip

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the application port
EXPOSE 80

# Define the command to run the Claude service
CMD ["python", "claude.py"]