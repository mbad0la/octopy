import requests,json

class followAPI(object):

    def __init__(self,token):
        self.AccessToken = token

    def my_followers(self):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/user/followers',headers=headers)
        return json.dumps(r.text)

    def get_followers(self,username):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/users/'+username+'/followers',headers=headers)
        return json.dumps(r.text)

    def my_following(self):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/user/following',headers=headers)
        return json.dumps(r.text)

    def get_following(self,username):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/users/'+username+'/following',headers=headers)
        return json.dumps(r.text)
