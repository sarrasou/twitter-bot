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

#website for scraping & headers
url = 'https://api.petfinder.com/v2/animals?type=cat&location=Buffalo, NY&status=adoptable&distance=20&sort=recent'
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA4NWNlZjlkODNiNGJlMDk0YjFhODc5NTY4YWE3OGY0MDhjMWNlOWVlYTJjMzVkYzI3YzU4M2JlZDY2ODdmMTA1OGJhM2YzOTg1MDM3MDFhIn0.eyJhdWQiOiI0Q2xPd2pwNk15MTJoY0xXN2pnamRXT3BFaEI1V0phVExWTkRGOElReDZaUlh3cXpqZiIsImp0aSI6IjA4NWNlZjlkODNiNGJlMDk0YjFhODc5NTY4YWE3OGY0MDhjMWNlOWVlYTJjMzVkYzI3YzU4M2JlZDY2ODdmMTA1OGJhM2YzOTg1MDM3MDFhIiwiaWF0IjoxNTY4MzIyODcyLCJuYmYiOjE1NjgzMjI4NzIsImV4cCI6MTU2ODMyNjQ3Miwic3ViIjoiIiwic2NvcGVzIjpbXX0.V-2y-VtT9CLJmmG47j8VbJic_fTSjteDCJp2kVMgMTdWkLOHpGeRT_mU4u118y7O5r-_78uIWM5vBuAVKSvxkuOzrxtRCHaC8mQBb0NH92XhRqNpOkoX0RAAzCrzd8Uyf0wqNZJTBgaxYY6KgVtG72ira9y6HJoJWeZaA-AixQoIKFf4KmsqA0AHQFXPJyJz5klEXSg8ax5szL5QfXiqvbvBlTa2HYbGIPksbr4F52pHgOXqsElLBQWK3TlHMca-ORWuVeKJty1NJp_-040KDVp2ESCftYkVP5J9laTJqP7saUkah14G5daL5nwQU_ZujlhZ3tgq4UbRs3Edr2EdtA'}

#download page for parsing
page = requests.get(url, headers=headers)
try:
    data = json.loads(page.text)
    # if data['status'] == "401"
    #     print("get new access token. use curl -d \"grant_type=client_credentials&client_id=4ClOwjp6My12hcLW7jgjdWOpEhB5WJaTLVNDF8IQx6ZRXwqzjf&client_secret=pYyK7ofztN5dhwBasAcasllE0ZElgBgRmCITjklX\" https://api.petfinder.com/v2/oauth2/token\" to get new authorization")
except ValueError:
    print("error loading JSON")

c = data['animals']
cat_data = c[0]

for cat in c:
    text = "My name is " + cat['name'] + " and I am adoptable! I am located in " + cat['contact']['address']['city'] + ". For more information: " + cat['url']
    # print(text)
    api.update_status(text)
    print("Tweeted: " + text)

    time.sleep(10)