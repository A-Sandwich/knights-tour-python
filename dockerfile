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
CMD ["python", "main.py"]
