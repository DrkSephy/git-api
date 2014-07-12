# Module for getting issues from a repository. 

import requests
import json
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

def get_all_issues(repositories):
    """
    Grabs a list of all issues from all public repositories of a User.

    Parameters:
    -----------
        repositories: A list containing all urls to grab issues from

    Returns:
    --------
        issues: A list containing all issues from a list of repositories of a user.
    """
    
    new_list =[]
    for repository in repositories:
        req_url = "https://api.github.com/repos/" + repository + "/issues" 
        req = requests.get(req_url)
        if req.status_code == 200:
            issues = json.loads(req.content)
            new_list.append(issues)
    return new_list

# Example of getting issues from one repository
# Get a list of issues at /DrkSephy/Deep-Learning
data = get_issues("https://api.github.com/repos/DrkSephy/Deep-Learning/issues")

# Example of getting issues from all of a user's public repositories
# Get a list of all of DrkSephy's repositories
url = "https://api.github.com/users/DrkSephy/repos"
request = requests.get(url)
repos = json.loads(request.content)
# Parse out the URLs from all the returned JSON. Returns a list of all repositories.
repositories = gitparsers.parse_repositories(repos)

# Pass list of repositories into get_all_issues method, returns a list of all issues in all repositories. 
all_issues = get_all_issues(repositories)
print all_issues




