'''
Send result of sentiment analysis to chosen slack channel
'''
import random
import config
import logging
import requests
import pandas as pd
from sqlalchemy import create_engine

# set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='../logs/log_bot.log', filemode='w'
)

# use create engine for making the connection to postgress db
engine = create_engine(config.conn_string)

# using sqlalchemy to select all rows from the sentiment table the database
selection = pd.read_sql('SELECT * FROM sentiment;', engine)

# use random number to post random twitter posts from the db
x = random.randint(0, 30)

# pick out the sentiment of the random tweet
senti = float(selection['sentiment'][x])

# post depending on the sentiment. about 0 pos below 0 neg and at 0 neutral
if senti > 0:
    requests.post(url=config.URL, json={
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Vader Sentiment analysis of a random tweet:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Tweet:*\n{selection['text'][x]}\n*When:*\n{selection['timestamp'][x]}\n*Vader Sentiment Value:* {senti}\n*Seems to be:* Positive\n"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://4.bp.blogspot.com/-x--m1C5hAyg/U51ZRPFFvTI/AAAAAAAABMo/6FF0bH4L2P4/s1600/4.jpg",
                    "alt_text": "computer thumbnail"
                }
    }]})
elif senti < 0:
    requests.post(url=config.URL, json={
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Vader Sentiment analysis of a random tweet:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Tweet:*\n{selection['text'][x]}\n*When:*\n{selection['timestamp'][x]}\n*Vader Sentiment Value:* {senti}\n*Seems to be:* Negitive\n"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://images.squarespace-cdn.com/content/566a4af357eb8d3974390587/1455451431849-3ZR52MOM2N35K0MU7XLM/image-asset.jpeg?content-type=image%2Fjpeg",
                    "alt_text": "computer thumbnail"
                }
    }]})
else:
    requests.post(url=config.URL, json={
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Vader Sentiment analysis of a random tweet:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Tweet:*\n{selection['text'][x]}\n*When:*\n{selection['timestamp'][x]}\n*Vader Sentiment Value:* {senti}\n*Seems to be:* Neutral\n"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/95a29505-23c9-4a16-972d-7487dc596931/d37tr27-c6e6605b-27d5-48bb-8f8a-dfbbfe669f13.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi85NWEyOTUwNS0yM2M5LTRhMTYtOTcyZC03NDg3ZGM1OTY5MzEvZDM3dHIyNy1jNmU2NjA1Yi0yN2Q1LTQ4YmItOGY4YS1kZmJiZmU2NjlmMTMucG5nIn1dXX0.zZC-R_FnOTvCzNYjPlnSj0bqnw3F7v329BdWe9JVuG8",
                    "alt_text": "computer thumbnail"
                }
    }]})
