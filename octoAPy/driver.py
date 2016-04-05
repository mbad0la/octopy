from endpoints import build_call
# import follow
from stargazers import starAPI
from events import eventsAPI
# import notifs
# import search

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

    def me(self):
        return self.authbearer

    def feed_for(self, entity = None, isorg = False):
        e = eventsAPI(self.authbearer["login"], self.authstring, self.istoken)
        if entity is not None:
            return e.get_feed(entity, isorg)
        else:
            if not isorg:
                return e.get_feed(self.authbearer["login"], False)
            else:
                return "Please set an organisation name to look for!"

    def stargazers_for(self, owner, repo):
        s = starAPI(self.authbearer["login"], self.authstring, self.istoken)
        return s.get_stargazers(owner, repo)

    def star(self, owner, repo):
        s = starAPI(self.authbearer["login"], self.authstring, self.istoken)
        return s.star_it(owner, repo)

    def unstar(self, owner, repo):
        s = starAPI(self.authbearer["login"], self.authstring, self.istoken)
        return s.unstar_it(owner, repo)
