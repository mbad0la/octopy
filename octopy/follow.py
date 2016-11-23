from endpoints import build_call

class followAPI(object):

    def __init__(self, username, authstring, token = False):
        self.requester = username
        self.authstring = authstring
        self.istoken = token

    def my_followers(self):
        return build_call("get", "user/followers", self.requester, self.authstring, {}, self.istoken)

    def get_followers(self,username):
        return build_call("get", "users/" + username + "/followers", self.requester, self.authstring, {}, self.istoken)

    def my_following(self):
        return build_call("get", "user/following", self.requester, self.authstring, {}, self.istoken)

    def get_following(self,username):
        return build_call("get", "users/" + username + "/following", self.requester, self.authstring, {}, self.istoken)
