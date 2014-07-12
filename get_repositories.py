# Module for getting a list of public repositories belonging to a User.

import requests
import simplejson as json
import gitparsers

# Github requests begin with: ""https://api.github.com/"

# Grab a list of my public repositories
req_url = "https://api.github.com/users/DrkSephy/repos"
# Make request
req = requests.get(req_url)
# Return JSON data
repos = json.loads(req.content)

# Sample Key:Value pair that we are interested in:
#   'full_name': 'DrkSephy/yabe'

data = gitparsers.parse_repositories(repos)
print data