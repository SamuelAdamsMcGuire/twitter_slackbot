FROM python:3.6-slim

WORKDIR /code_bot

COPY requirements.txt /code_bot
RUN pip install -r requirements.txt
#ADD . /slackbot

CMD ["python", "slackbot.py"]
