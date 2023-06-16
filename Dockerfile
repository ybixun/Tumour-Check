FROM python:3.10.9

# Set working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at the /app
ADD . /app

# Install any required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]


