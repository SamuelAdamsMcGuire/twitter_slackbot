# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /tweet_collector_1

COPY requirements.txt /tweet_collector_1
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /tweet_collector_1

# Run app.py when the container launches
CMD ["python", "tweets_git.py"]
