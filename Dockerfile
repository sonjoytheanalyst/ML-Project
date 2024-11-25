# Use a lightweight Python base image
FROM python:3.9-slim

# Update package index and install system dependencies
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    awscli \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Define the command to run the application
CMD ["python3", "app.py"]
