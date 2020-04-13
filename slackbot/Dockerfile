FROM python:3.6-slim

WORKDIR /slackbot

COPY requirements.txt /slackbot
RUN pip install -r requirements.txt
ADD . /slackbot

CMD ["python", "slackbot.py"]
