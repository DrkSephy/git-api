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
print data

# TODO: Return a parsed list of authors and commits in this form:
# commits: [ czhang: X, mk200789: Y, chessmasterhong: Z, DrkSephy: A]
