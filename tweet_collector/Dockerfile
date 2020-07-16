# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /code_tweet

# Get all needed requirements to fun environment
COPY requirements.txt /code_tweet
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "tweets_git.py"]
