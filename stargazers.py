import requests,json

class starAPI(object):

    def __init__(self,token):
        self.AccessToken = token

    def get_stargazers(self,RepoOwner,RepoName):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get("https://api.github.com/repos/"+RepoOwner+"/"+RepoName+"/stargazers",headers=headers)
        return json.dumps(r.text)
