import requests
import simplejson as json

# Github requests begin with: ""https://api.github.com/"

# Grab a list of my public repositories
req_url = "https://api.github.com/users/DrkSephy/repos"
# Make request
req = requests.get(req_url)
# Return JSON data
repos = json.loads(req.content)
# Display data
print repos