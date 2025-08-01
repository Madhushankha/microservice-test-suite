# Use Python 3.11 slim as the base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY . .

# Default command to run the test script
CMD ["python", "test_services.py"]
