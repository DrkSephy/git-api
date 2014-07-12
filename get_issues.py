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


def parse_all_issues(repos):
    """
    Returns the body content of all issues across a User's repositories.

    Parameters:
    -----------
        repos: A list of urls to query

    Returns:
    --------
        parsed_issues: A list containing the body content of all issues.

    """
    parsed_issues = []
    keys = ['body']
    for repository in repositories:
        req_url = "https://api.github.com/repos/" + repository + "/issues"
        req = requests.get(req_url)
        if req.status_code == 200 and req.content != '[]':
            data = json.loads(req.content)
            for a in data:
                for k,v in a.iteritems():
                    if k in keys:
                        if re.match('(.*?)(?=\s<)', v) == None:
                            parsed_issues.append(v)
                        else:
                            v2 = re.match('(.*?)(?=\s<)', v)
                            parsed_issues.append(v2.group())
    return parsed_issues

# Sample usage
print parse_all_issues(repositories)







