# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first to leverage Docker's caching mechanism
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Make the start_services.sh script executable
RUN chmod +x /app/start_services.sh

# Expose the ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
# For FastAPI

EXPOSE 8501
# For Streamlit

# Run the start_services.sh script to start both FastAPI and Streamlit
CMD ["sh", "start_services.sh"]
