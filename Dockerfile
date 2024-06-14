# Use the official Python image from the Alpine repository
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

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
EXPOSE 5000

# Run the application with Gunicorn
CMD ["gunicorn", "-b", "127.0.0.1:5000", "hbnb.setup:app"]
