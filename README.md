# Docker project

The goal of this project was building a datapipeline using DOCKER and getting to uderstand the ins and out of DOCKER better. I built 5 containers that work in series to a goal. The first container uses a python script to access the Twitter stream via their API. The stream filters tweets in relation to a specific topic and saves them in MongoDB. The second container is the connection with MongoDB. \
From here the data is accessed from a third container and then a sentiment analysis is preformed to rate the tweets from -1 to 1. One being very positive and negative one being very negative. The result and the original data is then uploaded to a PostgreSQL data-bank via the fourth docker container.The fifth and final container accesses the analyzed data and runs it through a simple python script that rates each tweet as positive, negative or neutral. This result is then posted to Slack via a Slockbot to a specificed channel in this case twitternews.     

## Requirements

Install Docker: \\
Docker is made so that programs written can be reproduced remotely by anyone around the world. Therefore the only requirement to run this script other than access tokens and codes to the various websites and databases is DOCKER. Docker will take care of the rest. What you will have to make sure is et up to your system is the docker-compose file. The neccessary portmapping, directory paths and passwords will need to be set for your system.

## Usage

Clone repo, add your personalise the config scripts with required data, ensure Slackchannel in slackbot script is set to the channel you want the results sent to. 

Then execute with the following in the CLI: 

docker-compose build <br>
docker-compose up

## Contributing
Pull requests are welcome. I am also very open to suggestions on how to improve the code.

## Sources
[twitter](https://developer.twitter.com/en/apps)
[Slack](www.slack.com)
