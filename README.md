git-api
=======

Repository for exploring Github's API: https://developer.github.com/v3/

Goals
=====

The end goal is to build something similar to Technetium: http://technetium.herokuapp.com/
This requires the following data: 
    
* Given a repository, return the number of commits made by each contributor. [Done]
* Given a repository, return the number of comments made by each contributor on all issues. 
* Given a repository, return the number of pull requests made by each contributor. 
* Given a repository, return the number of lines of code made by each contributor. [Done]
* Given a repository, return the number of comments made by each contributor for all pull requests. [Done]
* Given a repository, return the number of comments made by each contributor for all commits. [Done?]
* Given a repository, return the number of issues opened by each contributor. 
* Given a repository, return the number of issues closed by each contributor.
* Given a repository, return the number of issues assigned to each contributor. 
* Given a repository, return all issues. [Done]

While most of this data is already provided by Github, these scripts will help with building
our application.

Modules can be written in any language for quick testing, but in the end we will be using JavaScript.

Modules
=======

* `get_repositories.py`: Returns a listing of a user's public repositories. Useful for repository subscriptions in the future. 
* `gitparsers.py`: A set of parsers for working with data returned by the API.
* `get_issues.py`: Returns a listing of all issues for a given user. 
* `get_statistics.py`: Returns the number of commits for each contributor in a repository. 

Notes on testing
================

Github's API has a rate limit on the number of requests you can make per hour. 

* For unauthenticated requests, your rate limit is 60 requests/hr.
* For authenticated requests, your rate limit is 5,000 requests/hr. 

If your requests begin to fail and do not return anything, it means you have gone over your rate limit for the hour. 

You can read more about it here: https://developer.github.com/v3/#rate-limiting

To get around this, you can edit your requests as shown below:

    req_url = "https://api.github.com/users/DrkSephy/repos
    # Make request, where `user` = github username, `pass` = github password
    req = requests.get(req_url, auth=('user', 'pass'))
    # Return JSON data
    repos = json.loads(req.content)

    # Sample Key:Value pair that we are interested in:
    #   'full_name': 'DrkSephy/yabe'

    data = gitparsers.parse_repositories(repos)
    print data

**Please do not push any code with your password, remove those changes before committing!**

Another way to avoid low rate limits is to register an application through your github account settings page, and supply it inside of the request URL. An example is shown below:

    req_url = "https://api.github.com/users/DrkSephy/repos?client_id=xxxx&client_secret=yyyy'
    req = requests.get(req_url)
    # Return JSON data
    repos = json.loads(req.content)

    # Sample Key:Value pair that we are interested in:
    #   'full_name': 'DrkSephy/yabe'

    data = gitparsers.parse_repositories(repos)
    print data

**Please do not push any code with your client id or client secret, remove those changes before committing!**

