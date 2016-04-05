"""
Under work
import datetime,time

class searchAPI(object):

    def __init__(self,token):
        self.AccessToken = token

    def trending_repos(self):
        st = datetime.datetime.fromtimestamp(time.time()) - datetime.timedelta(days=10)
        st = st.strftime('%Y-%m-%dT%H:%M:%S')
        params = {'q':'created:>'+st,'sort':'stars','order':'desc','per_page':25}
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/search/repositories',headers=headers,params=params)
        return r.text
"""
