
FROM python:3.9-slim-buster

WORKDIR /app

# Copy the application files
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the script executable
RUN chmod +x bin-scan

# Set the entry point for the container
ENTRYPOINT ["./bin-scan"]
