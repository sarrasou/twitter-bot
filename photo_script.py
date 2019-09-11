#firstbot

import tweepy
import time
from time import sleep
import os
from config import *
import photo_dict

# Authorizes twitter app using credentials from config file
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#doactivity here
print("Welcome to twitter bot!")
photo_dict
os.chdir('kittens')
for kitten in os.listdir('.'):
    api.update_with_media(kitten)
    print("Photo posted:")
    print(kitten)

    try:
        os.remove(kitten)
        print("file removed")
    except:
        print("error removing file")

    time.sleep(60)
