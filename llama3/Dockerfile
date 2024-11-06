# Start with a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt into the image
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn for running the Flask app in production
# RUN pip install gunicorn

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 80

# Define the default command to run the application
CMD ["python", "llama3.py"]


# Define the default command to run the application with Gunicorn
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "llama3:app"]