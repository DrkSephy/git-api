# Module for getting issues from a repository. 

import requests
import simplejson as json

# Endpoint for getting issues from a repository: 
#           GET /repos/:owner/:repo/issues

# Pull data from one of my repositories
req_url = "https://api.github.com/repos/DrkSephy/Deep-Learning/issues"
# Make request
req = requests.get(req_url)
# Store issues
issues = json.loads(req.content)
print issues