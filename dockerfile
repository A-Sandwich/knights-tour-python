# Use an official Python runtime as a parent image
FROM python:3.13.1

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
# If you have requirements.txt, use:
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run your app
# Example if your entry point is app.py:
# https://stackoverflow.com/questions/29663459/why-doesnt-python-app-print-anything-when-run-in-a-detached-docker-container
CMD ["python", "-u", "main.py"]
