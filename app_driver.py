import requests,json

class octoAPy(object):
    def __init__(self,token):
        self.AccessToken = token
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/user',headers=headers)
        self.TokenBearer = json.loads(r.text)

    def owner(self):
        return json.dumps(self.TokenBearer)
