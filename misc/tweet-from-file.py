# Author : Yash Mehta <https://github.com/y-mehta/twitter-bot>
# Import Tweepy
import tweepy
# Import config file
from config import *
# Import sleep
from time import sleep

# Authorizes twitter app using credentials from config file
consumer_key = 'WhLlMIX9tbdjDWq4CZNGOn4M3'
consumer_secret = 'n9jkOZl6sokzqjFu23Rq1ug0vBJo9YaYqtnpMVvvnQFtbpNpTo'
access_token = '1167491810429689856-QqcQJVtG8CptNsY3afMuoqTgPXsd4w'
access_token_secret = 'xSZcGEMxtQqQuQC9CusqRSRxkvsH6VNTiqiO7FocEnaye'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file file.txt (or your chosen file)
auto_file = open('file.txt', 'r')

# Reads from txt file and assign it to a variable
read_file = auto_file.readlines()
auto_file.close()

# Loop to iterate and tweet a line at a time
for line_tweet in read_file:
    print(line_tweet)
    if line_tweet != '\n':
        api.update_status(line_tweet)
    else:
        pass

# Sleep Time, Should be >5 to avoid blocking
sleep(3600)
