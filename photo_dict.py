import requests
import os
import json
import tweepy
import time
from time import sleep
import os
from config import *

# Authorizes twitter app using credentials from config file
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#website for scraping
apiurl= "https://pixabay.com/api/?key=13586026-b8e36dbcdb0c4f3d2f358e519&q=kitten+cat+kittens+cats&per_page=50"

#download page for parsing
page = requests.get(apiurl)
try:
    data = json.loads(page.text)
except ValueError:
    print("error loading JSON")

# gets each image url and store in array
images = []
for each in data['hits']:
    images.append(each ['largeImageURL'])
    # print (images)


# create directory for image_tags
if not os.path.exists('kittens'):
    os.mkdir('kittens')
#move to new directory
os.chdir('kittens')

def write(i):
    x = 0
    #writing images
    for image in i:
        url = image
        source = requests.get(url)
        if source.status_code == 200:
            if not os.path.isfile('kitten-' + str(x) + '.jpg'):
                with open('kitten-' + str(x) + '.jpg', 'wb') as f:
                    f.write(source.content)
                    f.close()
                    x+=1
            else:
                x+=1        

write(images)

if len(os.listdir('.')) == 0:
    write(images)
for kitten in os.listdir('.'):
    api.update_with_media(kitten)
    print("Photo posted:")
    print(kitten)

    try:
        os.remove(kitten)
        print("file removed from folder")
    except:
        print("error removing file")

    # 3600 sec = 1 hour
    time.sleep(10)
