'''
Tap into twitter and stream tweets into mongoDB database
'''
import config
import tweepy
import time
import pymongo
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='../logs/log_tweets.log', filemode='w'
)

# authorization keys are called from a config file to get access to the
# twitter API see example config file for more info
auth = tweepy.OAuthHandler(config.CONSUMER_API_KEY, config.CONSUMER_API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Connect to Mongo locally or via docker
client = pymongo.MongoClient(config.mongo_conn)
# client = pymongo.MongoClient("mongodb://0.0.0.0:27017/")

# here the database is defined
db = client.twitter


# have tweepy listen in on the tweets and take the wanted attributes from them
class PrintStreamListener(tweepy.StreamListener):
    """
    https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py
    """

    def on_status(self, status):
        # specify what data should be captured from tweets
        tweet = {'date': status.created_at, 'text': status.text}
        # db.twitter.insert_many(tweet)
        db.tweets.insert_one(tweet)
        print(f'{status.created_at}: {status.text}')


# set up tweet stream
stream = tweepy.Stream(
    auth=auth,
    listener=PrintStreamListener())

# filter the stream to your chosen topic, language, filter level
stream.filter(
    track=['election'],
    languages=['en'],
    filter_level='low',
    is_async=True
)

# run stream for 5 seconds and then disconnect
time.sleep(5)
stream.disconnect()

logging.info('tweets collected')
