import slack
import random
import config
import pandas as pd
from sqlalchemy import create_engine 

#use create engine for making the connection to postgress db
engine = create_engine(config.conn_string)

#using sqlalchemy to select all rows from the sentiment table the database
selection = pd.read_sql('SELECT * FROM sentiment;', engine)

#use random number to post random twitter posts from the db
x = random.randint(0,30)

#make connection to slack
client = slack.WebClient(token=config.oauth_token)

#post depending on the sentiment. about 0 pos below 0 neg and at 0 neutral
if selection['sentiment'][x] > 0:
        client.chat_postMessage(channel='twitternews', text=f"The sentiment analyzer says that the tweet: {selection['text'][x]} is positive!")
elif selection['sentiment'][x] < 0:
        client.chat_postMessage(channel='twitternews', text=f"The sentiment analyzer says that the tweet: {selection['text'][x]} is negative")
else:
        client.chat_postMessage(channel='twitternews', text=f"The sentiment analyzer says that the tweet: {selection['text'][x]} is neutral")


