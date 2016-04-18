from endpoints import build_call
from follow import followAPI
from stargazers import starAPI
from events import eventsAPI
from notifs import notifAPI
from search import searchAPI

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

    def followers(self, username = None):
        f = followAPI(self.authbearer["login"], self.authstring, self.istoken)
        if username is None:
            return f.my_followers()
        else:
            return f.get_followers(username)

    def following(self, username = None):
        f = followAPI(self.authbearer["login"], self.authstring, self.istoken)
        if username is None:
            return f.my_following()
        else:
            return f.get_following(username)

    def notification(self, owner = None, repo = None):
        n = notifAPI(self.authbearer["login"], self.authstring, self.istoken)
        if owner is None and repo is None:
            return n.get_notifs()
        elif owner is not None and repo is not None:
            return n.repo_notif(owner, repo)
        else:
            return "[Missing Arguments]"

    def trend(self, days = 10, sort = "stars"):
        s = searchAPI(self.authbearer["login"], self.authstring, self.istoken)
        try:
            if sort == "stars" and int(days) > 0:
                return s.new_trending(days)
            else:
                return "[Second Argument Invalid]"
        except ValueError:
            return "[First Argument should be a Positive Integer]"
