from tinydb import TinyDB, Query
import os
import json
import requests

import ch_wal

dirname = os.path.dirname(__file__)
db_path = os.path.join(dirname, "storage/db.json")
# open db
uapi_db = TinyDB(db_path)
# read table for unsplash api
uapi_table = uapi_db.table('unsplash_api')
all_creds = uapi_table.all()

client_id = all_creds[0]['client_id']
client_secret = all_creds[1]['client_secret']
redirect_uri = all_creds[2]['redirect_uri']
code = all_creds[3]['code']

# where to save and load images
home_dir = os.environ['HOME']+"/"
wallpaper_folder = home_dir + ".wallpaper"
# for verbose debugging on cli
debug = False

if debug:
    print("client id: "+client_id)
    print("client secret: "+client_secret)
    print("redirect uri: "+redirect_uri)
    print("code: "+code)



input_two = input("Enter Image Keyword?: ")
""" print("You entered " + str(input_two))"""


#random = api.photo.random('collections=sci-fi')
#print(random)
# https://api.unsplash.com/photos/random?count=1
# https://api.unsplash.com/photos/K-qpIVj1aQ
p = api.search.photos(str(input_two))
print(p)
pid = p['results'][0].id
print("photo ID: "+pid)
print("wallpaper folder: "+wallpaper_folder)
photo_link = api.photo.download(pid)
print(photo_link)
r = requests.get(photo_link['url'])
path_to_save = str(wallpaper_folder)+"/"+str(pid)+".jpg"
with open(path_to_save, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

ch_wal.doit(wallpaper_folder, home_dir)