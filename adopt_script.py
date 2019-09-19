import requests
import os
import json
import tweepy
import time
from time import sleep
from config import *


def adopt_script():
    # Authorizes twitter app using credentials from config file
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    pf_data = {
        'grant_type': 'client_credentials',
        'client_id': '4ClOwjp6My12hcLW7jgjdWOpEhB5WJaTLVNDF8IQx6ZRXwqzjf',
        'client_secret': 'pYyK7ofztN5dhwBasAcasllE0ZElgBgRmCITjklX'
    }

    def get_pf_header():
        response = requests.post(
            'https://api.petfinder.com/v2/oauth2/token', data=pf_data)

        data = json.loads(response.text)
        access_token_pet_finder = data['access_token']

        pet_finder_headers = {
            'Authorization': 'Bearer ' + access_token_pet_finder}

        return pet_finder_headers

    # header
    # pet_finder_headers = {'Authorization': 'Bearer ' + access_token_pet_finder}
    pet_finder_headers = get_pf_header()

    # download page for parsing
    page = requests.get(pet_finder_url, headers=pet_finder_headers)
    data = json.loads(page.text)

    if 'status' in data:
        while 'status' in data:
            new_header = get_pf_header()
            page = requests.get(pet_finder_url, headers=new_header)
            data = json.loads(page.text)
    else:
        c = data['animals']
        # cat_data = c[0]

    for cat in c:
        text = "My name is " + cat['name'] + " and I am adoptable! I am located in " + \
            cat['contact']['address']['city'] + \
            ". For more information: " + cat['url']
        # print(text)
        try:
            api.update_status(text)
            print("Tweeted: " + text)

        except:
            print("error or duplicate tweet")
            continue

        time.sleep(60)


while True:
    adopt_script()
