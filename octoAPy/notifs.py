"""
Under work

class notifAPI(object):

    def __init__(self,token):
        self.AccessToken = token

    def get_notifs(self):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/notifications',headers=headers)
        return r.text

    def repo_notif(self,RepoOwner,RepoName):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/'+RepoOwner+'/'+RepoName+'/notifications',headers=headers)
        return r.text
"""
