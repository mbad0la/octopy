from endpoints import build_call

class notifAPI(object):

    def __init__(self, username, authstring, token = False):
        self.requester = username
        self.authstring = authstring
        self.istoken = token

    def get_notifs(self):
        return build_call("get", "notifications", self.requester, self.authstring, {}, self.istoken)

    def repo_notif(self, owner, name):
        return build_call("get", "repos/" + owner + "/" + name + "/notifications", self.requester, self.authstring, {}, self.istoken)
