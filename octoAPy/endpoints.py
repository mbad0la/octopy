import requests, json, base64

api_url = "https://api.github.com/"

def build_call(method, endpoint, username, authstring, params = {}, token = False):
    headers = None
    if method == "get":
        if not token:
            headers = { 'Authorization': 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Accept': 'application/json', 'Content-Type': 'application/json' }
        else:
            headers = { 'Authorization': 'token ' + authstring, 'Accept': 'application/json', 'Content-Type': 'application/json' }
        r = requests.get(api_url + endpoint, headers = headers, params = params)
        return json.loads(r.text)
    elif method == "post":
        if not token:
            headers = { 'Authorization': 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Accept': 'application/json', 'Content-Type': 'application/json' }
        else:
            headers = { 'Authorization': 'token ' + authstring, 'Accept': 'application/json', 'Content-Type': 'application/json' }
        r = requests.post(api_url + endpoint, headers = headers, data = json.dumps(params))
        return json.loads(r.text)
    elif method == "put":
        if not token:
            headers = { 'Authorization': 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Content-length': 0, 'Accept': 'application/json', 'Content-Type': 'application/json' }
        else:
            headers = { 'Authorization': 'token ' + authstring, 'Content-length': 0, 'Accept': 'application/json', 'Content-Type': 'application/json' }
        r = requests.put(api_url + endpoint, headers = headers, params = params)
        return r.status_code
    elif method == "delete":
        if not token:
            headers = { 'Authorization': 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (username,authstring)), 'Content-length': 0, 'Accept': 'application/json', 'Content-Type': 'application/json' }
        else:
            headers = { 'Authorization': 'token ' + authstring, 'Content-length': 0, 'Accept': 'application/json', 'Content-Type': 'application/json' }
        r = requests.delete(api_url + endpoint, headers = headers, params = params)
        return r.status_code
