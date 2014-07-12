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

# The keys we are interested in parsing out are:
#   'full_name': 'DrkSephy/yabe'

def parse_repositories(data):
    """
    Parses returned JSON for the API call to the `repos` endpoint. 

    Parameters:
    ----------
    data: JSON data returned from the endpoint. 

    Returns:
    --------
    repositories: dictionary
        - A JSON formatted dictionary containing repository endpoints.
    """

    keys = ['full_name']
    repositories = []

    for a in data:
        new_list = {}
        for k,v in a.iteritems():
            if k in keys:
                if re.match('(.*?)(?=\s<)', v) == None:
                    new_list[k] = v
                else:
                    v2 = re.match('(.*?)(?=\s<)', v)
                    new_list[k] = v2.group() 
        repositories.append(new_list)
    return repositories

data = parse_repositories(repos)
print data