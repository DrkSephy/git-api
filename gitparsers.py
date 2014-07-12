# Module containing parsers for data returned by Github's API.

import re

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
                    repositories.append(v)
                else:
                    v2 = re.match('(.*?)(?=\s<)', v)
                    repositories.append(v2.group())
    return repositories