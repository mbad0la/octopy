from endpoints import build_call

class eventsAPI(object):

    def __init__(self, username, authstring, token = False):
        self.requester = username
        self.authstring = authstring
        self.istoken = token

    def get_feed(self, entity, isorg):
        if not isorg:
            return build_call("get", "users/" + entity + "/received_events", self.requester, self.authstring, {}, self.istoken)
        else:
            return build_call("get", "orgs/" + entity + "/events", self.requester, self.authstring, {}, self.istoken)
