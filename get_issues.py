# Module for getting issues from a repository. 

import requests
import json
import gitparsers

# Endpoint for getting issues from a repository: 
#           GET /repos/:owner/:repo/issues

# Pull data from one of my repositories
#req_url = "https://api.github.com/repos/DrkSephy/Deep-Learning/issues"
# Make request
#req = requests.get(req_url)
# Store issues
#issues = json.loads(req.content)
#print issues


url = "https://api.github.com/users/DrkSephy/repos
request = requests.get(url)
repos = json.loads(request.content)
repositories = gitparsers.parse_repositories(repos)

new_list = []
for repository in repositories:
    req_url = "https://api.github.com/repos/" + repository + "/issues" 
    req = requests.get(req_url)
    if req.status_code == 200:
        issues = json.loads(req.content)
        new_list.append(issues)

print new_list




