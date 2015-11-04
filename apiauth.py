import requests,json,base64
import app_driver
# Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.
# by @kennethreitz
class Authwrapper(object):
    def __init__(self,client_id,client_secret,note):
        self.ClientId = client_id
        self.ClientSecret = client_secret
        self.note = note

    def authenticate(self,username,password,scopes=[]):
        headers={'Authorization':'Basic '+base64.urlsafe_b64encode("%s:%s" % (username,password)),'Accept':'application/json','Content-Type':'application/json'}
        options={'note':self.note,'client_id':self.ClientId,'client_secret':self.ClientSecret,'fingerprint':username,'scopes':scopes}
        r = requests.post("https://api.github.com/authorizations",headers=headers,data=json.dumps(options))
        return app_driver.octoAPy(json.loads(r.text)['token'])
