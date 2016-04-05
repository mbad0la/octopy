from endpoints import build_call

class starAPI(object):

    def __init__(self, username, authstring, token = False):
        self.requester = username
        self.authstring = authstring
        self.istoken = token

    def get_stargazers(self, owner, name):
        return build_call("get", "repos/" + owner + "/" + name + "/stargazers", self.requester, self.authstring, {}, self.istoken)

    def star_it(self, owner, name):
        return build_call("put", "user/starred/" + owner + "/" + name, self.requester, self.authstring, {}, self.istoken)

    def unstar_it(self, owner, name):
        return build_call("delete", "user/starred/" + owner + "/" + name, self.requester, self.authstring, {}, self.istoken)
