# Module for getting issues from a repository. 

import requests
import simplejson as json


req_url = "https://api.github.com/repos/DrkSephy/Deep-Learning/issues"
req = requests.get(req_url)
issues = json.loads(req.content)
print issues