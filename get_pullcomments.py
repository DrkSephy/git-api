# Module for getting pull request comments from a repository. 

import requests
import json

def parse_all_comments(): 

    comments = []
    keys = ['body']
    count = 0
    #req_url = "https://api.github.com/repos/chessmasterhong/WaterEmblem/issues/comments"
    req_url = "https://api.github.com/repos/DrkSephy/git-api/issues/comments"
    req = requests.get(req_url)
    if req.status_code == 200 and req.content != '[]':
        data = json.loads(req.content)
        for a in data:
            for k,v in a.iteritems():
                if k in keys:
                    count +=1
                    comments.append(v)

    return comments

# Sample usage
print parse_all_comments()







