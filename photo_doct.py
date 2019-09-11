import requests
from bs4 import BeautifulSoup as soup
import os
import json

#website for scraping
apiurl= "https://pixabay.com/api/?key=13586026-b8e36dbcdb0c4f3d2f358e519&q=kitten+cat+kittens+cats"

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

# image filename variable
x = 0
#writing images
for image in images:
    url = image
    source = requests.get(url)
    if source.status_code == 200:
        with open('kitten-' + str(x) + '.jpg', 'wb') as f:
            f.write(source.content)
            f.close()
            x+=1
