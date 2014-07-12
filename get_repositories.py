# Module for getting a list of public repositories belonging to a User.

import re
import requests
import simplejson as json

# Github requests begin with: ""https://api.github.com/"

# Grab a list of my public repositories
req_url = "https://api.github.com/users/DrkSephy/repos"
# Make request
req = requests.get(req_url)
# Return JSON data
repos = json.loads(req.content)

# Sample Key:Value pair that we are interested in:
#   'full_name': 'DrkSephy/yabe'

def parse_repositories(data):
    """
    Parses returned JSON for the API call to the `repos` endpoint. 

    Parameters:
    ----------
    data: JSON data returned from the endpoint. 

    Returns:
    --------
    repositories: list
        - A JSON formatted list containing repository endpoints.
    """

    keys = ['full_name']
    repositories = []

    for a in data:
        new_list = {}
        for k,v in a.iteritems():
            if k in keys:
                if re.match('(.*?)(?=\s<)', v) == None:
                    repositories.append("https://github.com/" + v)
                else:
                    v2 = re.match('(.*?)(?=\s<)', v)
                    repositories.append("https://github.com/" + v2.group())
    return repositories

data = parse_repositories(repos)
print data