# Module for exploring Github statistics. 
# API endpoint for statistics: GET /repos/:owner/:repo/stats/contributors
# Returns JSON containing the `total` number of commits for each user in the 
# repository. 

# Samole JSON returned from: "https://api.github.com/repos/chessmasterhong/WaterEmblem/stats/contributors"

#  'total': 464,
#    'author': {
#        'following_url': 'https://api.github.com/users/chessmasterhong/following{/other_user}',
#        'events_url': 'https://api.github.com/users/chessmasterhong/events{/privacy}',
#        'organizations_url': 'https://api.github.com/users/chessmasterhong/orgs',
#        'url': 'https://api.github.com/users/chessmasterhong',
#        'gists_url': 'https://api.github.com/users/chessmasterhong/gists{/gist_id}',
#        'html_url': 'https://github.com/chessmasterhong',
#        'subscriptions_url': 'https://api.github.com/users/chessmasterhong/subscriptions',
#        'avatar_url': 'https://avatars.githubusercontent.com/u/1214945?',
#        'repos_url': 'https://api.github.com/users/chessmasterhong/repos',
#        'received_events_url': 'https://api.github.com/users/chessmasterhong/received_events',
#        'gravatar_id': None,
#        'starred_url': 'https://api.github.com/users/chessmasterhong/starred{/owner}{/repo}',
#        'site_admin': False,
#        'login': 'chessmasterhong',
#        'type': 'User',
#        'id': 1214945,
#       'followers_url': 'https://api.github.com/users/chessmasterhong/followers'
#    }

import re
import requests
import simplejson as json

req_url = "https://api.github.com/repos/DrkSephy/WaterEmblem/stats/contributors"
req = requests.get(req_url)
data = json.loads(req.content)

def parse_commits(commits):
    parsed_authors = []

    for commit in commits:
        data = {}
        data['author'] = commit['author']['login']
        data['commits'] = commit['total']
        parsed_authors.append(data)
    return parsed_authors

print parse_commits(data)
# Returns: 
# [{'commits': 3, 'author': 'czhang'}, {'commits': 28, 'author': 'mk200789'}, 
#  {'commits': 294, 'author': 'DrkSephy'}, {'commits': 464, 'author': 'chessmasterhong'}]
