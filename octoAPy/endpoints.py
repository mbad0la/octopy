import requests, json, base64

api_url = "https://api.github.com/"

def build_call(method, endpoint, username, authstring, params = {}, token = False):
    headers = None
    if method == "get":
        if token == False:
            headers = { 'Authorization': 'Basic '+base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Accept': 'application/json', 'Content-Type': 'application/json' }
        else:
            headers = { 'Authorization': 'token '+base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Accept': 'application/json', 'Content-Type': 'application/json' }
        r = requests.get(api_url + endpoint, headers = headers, params = {})
        return json.loads(r.text)
    elif method == "post":
        if token == False:
            headers = { 'Authorization': 'Basic '+base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Accept': 'application/json', 'Content-Type': 'application/json' }
        else:
            headers = { 'Authorization': 'token '+base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Accept': 'application/json', 'Content-Type': 'application/json' }
        r = requests.post(api_url + endpoint, headers = headers, data = json.dumps(params))
        return json.loads(r.text)
