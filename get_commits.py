import requests
import simplejson as json

req_url = "https://api.github.com/repos/DrkSephy/WaterEmblem/commits?DrkSephy"
req = requests.get(req_url)
commits = json.loads(req.content)
print commits