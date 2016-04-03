from endpoints import build_call
import follow
import stargazers
import events
import notifs
import search

class octoAPy(object):

    def __init__(self, username, authstring, token = False):
        self.authstring = authstring
        self.istoken = token
        self.authbearer = build_call("get", "user", username, authstring, {}, token)

    def get_token(self, clientid, clientsecret):
        options = { 'note': "get-me-token", 'client_id': clientid,'client_secret': clientsecret,'fingerprint': self.authbearer["login"], 'scopes': []}
        if self.istoken:
            return self.authstring
        else:
            r = build_call("post", "authorizations", self.authbearer["login"], self.authstring, options)
            try:
                self.authstring = r['token']
                self.istoken = True
                return self.authstring
            except:
                return "You already have a token corresponding to this app!"
