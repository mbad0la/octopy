import requests,json,base64,_mysql
import app_driver
# Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.
# by @kennethreitz

class Authwrapper(object):
    
    def __init__(self,client_id,client_secret,note):
        self.ClientId = client_id
        self.ClientSecret = client_secret
        self.note = note

    def authenticate(self,username,authorized,authstring,scopes=[]):
        if authorized == 1:
            conn = _mysql.connect(HOST_NAME,MYSQL_USERNAME,MYSQL_PASS,DB_NAME)
            conn.query("SELECT token from "+TABLE_NAME+" where login = '"+username+"'")
            result = conn.store_result()
            tkn = result.fetch_row(1)
            if tkn[0][0] == authstring:
                return app_driver.octoAPy(tkn[0][0])
            else:
                return app_driver.octoAPy(None)
        else:
            headers={'Authorization':'Basic '+base64.urlsafe_b64encode("%s:%s" % (username,authstring)),'Accept':'application/json','Content-Type':'application/json'}
            options={'note':self.note,'client_id':self.ClientId,'client_secret':self.ClientSecret,'fingerprint':username,'scopes':scopes}
            r = requests.post("https://api.github.com/authorizations",headers=headers,data=json.dumps(options))
            if r.status_code != 201:
                conn = _mysql.connect(HOST_NAME,MYSQL_USERNAME,MYSQL_PASS,DB_NAME)
                conn.query("SELECT token from "+TABLE_NAME+" where login = '"+username+"'")
                result = conn.store_result()
                tkn = result.fetch_row(1)
                return app_driver.octoAPy(tkn[0][0])
            else:
                tkn = json.loads(r.text)['token']
                conn = _mysql.connect(HOST_NAME,MYSQL_USERNAME,MYSQL_PASS,DB_NAME)
                conn.query("INSERT INTO "+TABLE_NAME+" VALUES('"+username+"','"+tkn+"')")
                return app_driver.octoAPy(tkn)
