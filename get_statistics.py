# Module for exploring Github statistics. 
# API endpoint for statistics: GET /repos/:owner/:repo/stats/contributors

import requests
import simplejson as json

req_url = "https://api.github.com/repos/DrkSephy/Deep-Learning/stats/commit_activity"
req = requests.get(req_url)
data = json.loads(req.content)
print data