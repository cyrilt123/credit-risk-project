# Use the official Python image as the base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the app and required files into the container
COPY ./app /app
COPY ./outputs /app/outputs

# Install Python dependencies with specific scikit-learn version
RUN pip install flask pandas scikit-learn==1.3.2

RUN pip install flask flask-cors


# Expose the port the app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
