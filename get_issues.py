# Module for getting issues from a repository. 

import requests
import json
import re
import gitparsers

def get_issues(url):
    """
    Grabs all issues from a single repository.

    Parameters:
    -----------
        url: Github endpoint to pull issues from.

    Returns:
    -------
        issues: List containing all issues from a repository.
    """
    req_url = url
    req = requests.get(req_url)
    issues = json.loads(req.content)
    return issues

def parse_all_issues(repositories):
    """
    Grabs a list of all issues from all public repositories of a User.

    Parameters:
    -----------
        repositories: A list containing all urls to grab issues from

    Returns:
    --------
        issues: A list containing all issues from a list of repositories of a user.
    """
    
    parsed_issues = []
    for repository in repositories:
        req_url = "https://api.github.com/repos/" + repository + "/issues" 
        req = requests.get(req_url)
        if req.status_code == 200 and req.content != '[]' and req.content != 'None':
            issues = json.loads(req.content)
            print issues




# Example of getting issues from one repository
# Get a list of issues at /DrkSephy/Deep-Learning
data = get_issues("https://api.github.com/repos/DrkSephy/Deep-Learning/issues")
# print data

# Example of getting issues from all of a user's public repositories
# Get a list of all of DrkSephy's repositories
url = "https://api.github.com/users/DrkSephy/repos"
request = requests.get(url)
repos = json.loads(request.content)
# Parse out the URLs from all the returned JSON. Returns a list of all repositories.
repositories = gitparsers.parse_repositories(repos)


def parse_one_issue(data):
    parsed_issues = []
    keys = ['body']
    for a in data:
        for k,v in a.iteritems():
            if k in keys:
                if re.match('(.*?)(?=\s<)', v) == None:
                    parsed_issues.append(v)
                else:
                    v2 = re.match('(.*?)(?=\s<)', v)
                    parsed_issues.append(v2.group())
    return parsed_issues

print parse_one_issue(data)






