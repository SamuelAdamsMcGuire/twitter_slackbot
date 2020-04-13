import config
import tweepy
import time
import pymongo

# authorization keys are called from a config file to get access to the twitter API
#see example config file for more info
auth = tweepy.OAuthHandler(config.CONSUMER_API_KEY, config.CONSUMER_API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

#hconnect to Mongodb. I had two clients defined so that I could do isolated/local tests
client = pymongo.MongoClient(config.mongo_conn)
#client = pymongo.MongoClient("mongodb://0.0.0.0:27018/")

#here the database is defined
db = client.twitter

#have tweep listen in on the tweets and take the wanted attributes from them.
class PrintStreamListener(tweepy.StreamListener):
    """
    https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py
    """   

    def on_status(self, status):
        # do something with incoming tweets
        tweet={'date':status.created_at, 'text':status.text}
        db.twitter.insert_one(tweet)
        print(f'{status.created_at}: {status.text}')

#set up tweet stream 
stream = tweepy.Stream(
    auth = auth, 
    listener=PrintStreamListener())

#filter the stream to your chosen topic, language,
stream.filter(
    track=['corona'],
    languages=['en'],
    filter_level='low', 
    is_async=True
)

# run stream for 5 seconds and then disconnect
time.sleep(5)
stream.disconnect()
