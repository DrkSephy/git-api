# Module for getting pull comments from a repository. 

import requests
import json

def parse_pull_comments(): 

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

    return comments, data



#Given a repository, return the number of comments made by each contributor for all pull requests
def parse_pull_comments_count(): 

    comments_count = []
    users = {}
    keys = ['user']
    count = 0
    req_url = "https://api.github.com/repos/chessmasterhong/WaterEmblem/issues/comments"
    #req_url = "https://api.github.com/repos/DrkSephy/git-api/issues/comments"
    req = requests.get(req_url)
    if req.status_code == 200 and req.content != '[]':
        data = json.loads(req.content)
        for a in data:
            for k,v in a.iteritems():
                if k in keys:
                    if v['login'] in users:
                        count +=1
                        users[v['login']]+=1
                    else:
                        users[v['login']]=1

    comments_count.append(users)

    return comments_count

# Sample usage
print parse_pull_comments_count()

print parse_pull_comments()



