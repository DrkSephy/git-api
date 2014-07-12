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




