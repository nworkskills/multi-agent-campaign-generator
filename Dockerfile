# Use official Python runtime as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Expose port for Gradio (if using UI) or FastAPI
EXPOSE 7860

# Run the application
CMD ["python", "campaign_generator.py"]