import requests
import json


headers = {"content-type": "application/json"}
req = requests.get("https://itunes.apple.com/search?term=clark&country=JP&media=music&",headers=headers).json()

p = json.dumps(req,indent=4)
print(p)