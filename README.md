# Docker project

The goal of this project was getting build a datapipeline using DOCKER. I built 5 containers that would work in series to a goal. The first container would use a python script to access Twitter stream via their API. The stream filters tweets in relation to a specific topic and saves them in MongoDB. The second container is the connection with MongoDB. From here the data is accessed from a third container and then a sentiment analysis would be preformed to rate the tweets from -1 to 1. One being very positive and negative one being very negative. The result and the original data is then uploaded to a PostgreSQL data-bank.The fourth and final container accesses the analyzed data and run it through a simple python script that would rate each tweet as positive, negative or neutral. This result is then posted to Slack via a Slockbot to a specificed channel in my case twitternews.     

## Requirements

Install Docker:
Docker is made so that programs written can be reproduced remotely by anyone around the world. Therefor the only requirement to run this script other than access tokens and codes to the various websites and databases is DOCKER. Docker will take care of the rest. What you will have to make sure is et up to your system is the docker-compose file. The neccessary portmapping, directory paths and passwords will need to be set for your system.

## Usage

Clone repo, add your personal config script with required data, ensure Slackchannel in slackbot script is set to the channel you want the results sent to. 

Then execute with the following in the CLI: 

docker-compose build <br>
docker-compose up

## Contributing
Pull requests are welcome. I am also very open to suggestions on how to improve the code.

## Sources
[twitter](https://developer.twitter.com/en/apps)
[Slack](www.slack.com)
