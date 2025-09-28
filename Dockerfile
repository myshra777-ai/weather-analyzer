# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV DEFAULT_CITY=Indore
ENV LOG_FILE=/output/weather_log.txt
ENV DATA_FILE=/output/weather_data.csv

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

