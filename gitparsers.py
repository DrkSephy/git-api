# Module containing parsers for data returned by Github's API.

import re

def parse_repositories(data, keys):
    """
    Parses returned JSON for the API call to the `repos` endpoint. 

    Parameters:
    ----------
    data: JSON data returned from the endpoint. 
    keys: The keys we are interested in parsing out of the JSON.

    Returns:
    --------
    repositories: list
        - A JSON formatted list containing repository endpoints.

    Usage: 
        - To parse a key from a repository, supply it in the function call.
        - For repositories, we want to parse out the 'full_name' key. 
        - For issues in a repository, we want to parse out the 'body' key.
    """

   
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