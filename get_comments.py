# Module for getting issues from a repository. 

import requests
import json
import re
import gitparsers


# Example of getting issues from all of a user's public repositories
# Get a list of all chessmasterhong's repositories
url = "https://api.github.com/users/chessmasterhong/repos"
#request = requests.get(url, auth=('user', 'pw'))
request = requests.get(url)
repos = json.loads(request.content)
# Parse out the URLs from all the returned JSON. Returns a list of all repositories.
repositories = gitparsers.parse_repositories(repos)

def parse_all_comments(repos): 

    parsed_comments = []
    users ={}
    keys = ['user']
    for repository in repositories:
        req_url = "https://api.github.com/repos/" + repository + "/comments"
        req = requests.get(req_url)
        if req.status_code == 200 and req.content != '[]':
            data = json.loads(req.content)
            for a in data:
                for k,v in a.iteritems():
                    if k in keys:
                        if v['login'] in users:
                            users[v['login']]+=1
                        else:
                            users[v['login']]=1
                            
    parsed_comments.append(users)

    return parsed_comments

# Sample usage
print parse_all_comments(repositories)







