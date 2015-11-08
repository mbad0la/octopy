import requests,json
import follow
import stargazers
import events
import notifs
import search

class octoAPy(object):
    
    def __init__(self,token):
        self.AccessToken = token
        headers={'Authorization':'token '+self.AccessToken,'Accept':'application/json','Content-Type':'application/json'}
        r = requests.get('https://api.github.com/user',headers=headers)
        self.TokenBearer = json.loads(r.text)
    
    def get_token(self):
        return json.dumps(self.AccessToken)
        
    def owner(self):
        return json.dumps(self.TokenBearer)
        
    def follower_driver(self,username = None):
        f = follow.followAPI(self.AccessToken)
        if username is None:
            return f.get_followers(self.TokenBearer['login'])
        else:
            return f.get_followers(username)

    def following_driver(self,username = None):
        f = follow.followAPI(self.AccessToken)
        if username is None:
            return f.get_following(self.TokenBearer['login'])
        else:
            return f.get_following(username)
            
    def stargazer_driver(self,RepoOwner,RepoName):
        s = stargazers.starAPI(self.AccessToken)
        return s.get_stargazers(RepoOwner,RepoName)
        
    def event_driver(self,username = None):
        e = events.eventsAPI(self.AccessToken)
        if username is None:
            return e.get_events(self.TokenBearer['login'])
        else:
            return e.get_events(username)
            
    def notif_driver(self):
        n = notifs.notifAPI(self.AccessToken)
        return n.get_notifs()
        
    def reponotif_driver(self,RepoOwner,RepoName):
        n = notifs.notifAPI(self.AccessToken)
        return n.repo_notif(RepoOwner,RepoName)
        
    def trending_driver(self):
        srch = search.searchAPI(self.AccessToken)
        return srch.trending_repos()
