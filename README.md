# octoAPy
### Python wrapper for Github API

Easy to use methods for using Github API in your favourite language python!

##### Let's start!

```python
import app_driver

apiobj = app_driver.octoAPy("mbad0la_token")
print apiobj.owner()
"""
Response :
{"disk_usage": 367, "private_gists": 0, "public_repos": 8, "site_admin": false, "subscriptions_url": "https://api.github.com/users/mbad0la/subscriptions", "gravatar_id": "", "hireable": null, "id": 8503331, "followers_url": "https://api.github.com/users/mbad0la/followers", "following_url": "https://api.github.com/users/mbad0la/following{/other_user}", "collaborators": 0, "total_private_repos": 0, "blog": null, "followers": 3, "location": null, "type": "User", "email": null, "bio": null, "gists_url": "https://api.github.com/users/mbad0la/gists{/gist_id}", "owned_private_repos": 0, "company": null, "events_url": "https://api.github.com/users/mbad0la/events{/privacy}", "html_url": "https://github.com/mbad0la", "updated_at": "2015-12-04T11:35:11Z", "plan": {"collaborators": 0, "name": "free", "private_repos": 0, "space": 976562499}, "received_events_url": "https://api.github.com/users/mbad0la/received_events", "starred_url": "https://api.github.com/users/mbad0la/starred{/owner}{/repo}", "public_gists": 0, "name": "Mayank Badola", "organizations_url": "https://api.github.com/users/mbad0la/orgs", "url": "https://api.github.com/users/mbad0la", "created_at": "2014-08-20T13:52:15Z", "avatar_url": "https://avatars.githubusercontent.com/u/8503331?v=3", "repos_url": "https://api.github.com/users/mbad0la/repos", "following": 16, "login": "mbad0la"}
"""
```

Similar easy the use methods to  fulfill your requirements.

Read the [Docs]() to know about all available awesomeness.


#### Authentication

API methods need authentication( many of them or they have rate limiting issues ). Thus a basic authentication method is also provided.

You need to get Client ID and Client secret to use authentication in your app. Read more about it [here](https://developer.github.com/v3/oauth/).

```python
import apiauth
authobj = apiauth.Authwrapper("client_id","client_secret","application_use")
apiobj = authobj.authenticate(username,[0|1],[password|token],scopes)
# for authentication with parameter 0, password is provided with username and on validation an api object is returned.
# for authentication with parameter 1, token is provided with username to match with the data stored in the database and upon validation an api object is returned.
# scopes is a list that contains permissions to be given to a new token.

print apiobj.owner()

```

#### Contributing

As a lot of API endpoints are yet uncovered, any contribution to include more endpoints is much appreciated. It would be appreciated if pull requests follow the coding practices used in the project. It would allow me to merge your requests quicker and maintain code readability.
