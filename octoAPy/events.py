import requests

class eventsAPI(object):

    def __init__(self,token):
        self.AccessToken = token

    def get_events(self,username):
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/users/'+username+'/received_events',headers=headers)
        return r.text
