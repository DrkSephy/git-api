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




