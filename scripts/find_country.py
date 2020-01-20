#!/home/mefath5/.local/bin/python3

from os import environ
import requests
import json

try:
    # if "REMOTE_ADDR" in environ:
    user_ip = environ["REMOTE_ADDR"]
    ur = "http://api.ipstack.com/5.102.236.176?access_key=c4e56f168a3eb0af77fea9b9514bd80c"   
    url = "http://api.ipstack.com/" +user_ip+ "?access_key=c4e56f168a3eb0af77fea9b9514bd80c"

    ret = requests.get(url)
    view = ret.json()["country_code"]
    
except:
	view = json.dumps("error")

print("Content-Type: text/plain\n")
print(view)