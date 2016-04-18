from endpoints import build_call
import datetime,time

class searchAPI(object):

    def __init__(self, username, authstring, token = False):
        self.requester = username
        self.authstring = authstring
        self.istoken = token

    def new_trending(self, days):
        st = datetime.datetime.fromtimestamp(time.time()) - datetime.timedelta(days = days)
        st = st.strftime('%Y-%m-%dT%H:%M:%S')
        params = { 'q': 'created:>'+st, 'sort': 'stars', 'order': 'desc', 'per_page': 25 }
        return build_call("get", "search/repositories", self.requester, self.authstring, params, self.istoken)
