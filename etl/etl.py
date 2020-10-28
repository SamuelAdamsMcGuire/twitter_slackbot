'''
Extract tweets from mongoDB, transform them via a sentiment analysis, 
then load them into postgresqlDB
'''
import logging
import pymongo
import config
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sqlalchemy import create_engine

# set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='../logs/log_etl.log', filemode='w'
)

# connect to mongodb locally or via docker
# mdb = pymongo.MongoClient("mongodb://0.0.0.0:27018/")
mdb = pymongo.MongoClient(config.mongo_conn)
logging.info(mdb)

# collect results
result = mdb.twitter.tweets.find()

# set up sentiment analyzer
s = SentimentIntensityAnalyzer()

# loop through the cursor object retrieved from Mongodb and extract wanted data
tweet_list = []
for docs in result:
    sentiment = s.polarity_scores(docs['text'])['compound']
    row = (docs['text'], sentiment, docs['date'])
    tweet_list.append(row)

logging.info(tweet_list)
# put the list into a pandas dataframe
df = pd.DataFrame(tweet_list, columns=['text', 'sentiment', 'timestamp'])
logging.info(df)

db = create_engine(f'{config.post_conn}sentiment_db')

# set up for exceptions for connection
try:
    df.to_sql('sentiment', db, if_exists='append', index=False)
    logging.info('db updated')
except ConnectionError:
    logging.exception('Connection not made!')
