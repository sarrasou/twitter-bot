#firstbot

import tweepy
import time
import os
from config import *
from time import sleep

# Authorizes twitter app using credentials from config file
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#doactivity here
print("Welcome to twitter bot!")
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
#api.update_status("words")
