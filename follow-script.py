# Author : Yash Mehta <https://github.com/y-mehta/twitter-bot>
# Import Tweepy
import tweepy
# Import config file
from config import *
# Import sleep
from time import sleep

# Authorizes twitter app using credentials from config file
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print(tweepy.Cursor(api.search, q='#kitten').items())
# for tweet in tweepy.Cursor(api.search, q='#kitten').items():
#     try:
#         print('@' + tweet.user.screen_name + ' tweeted : ' + tweet.text)
#         if not tweet.user.following:
#             tweet.user.follow()
#             print('Followed')
#             sleep(10)

#     except tweepy.TweepError as error:
#         print(error.reason)

#     except StopIteration:
#         break
