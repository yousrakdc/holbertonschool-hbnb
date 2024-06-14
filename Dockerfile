# Use the official Python image from the Alpine repository
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /hbnb

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /hbnb

# Create a volume for persistent storage
VOLUME [ "/data" ]

# Expose the port the app runs on
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "hbnb:app"]
