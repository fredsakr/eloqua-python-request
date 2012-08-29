import base64
import urllib
import urllib2

class EloquaRequest(urllib2.Request):
    headers = ''
    base_url = 'https://secure.eloqua.com/API/REST/1.0'

    def __init__(self, site, user, password):
        authKey = base64.b64encode(site + "\\" + user + ":" + password)
        self.headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

    def get(self, url, data):
        return self.request('GET', url, data)

    def post(self, url, data):
        return self.request('POST', url, data)

    def put(self, url, data):
        return self.request('PUT', url, data)

    def delete(self, url, data):
        return self.request('DELETE', url, data)

    def request(self, method, url, data):
        request_object = urllib2.Request(self.base_url + url)
        request_object.get_method = lambda: method

        for key,value in self.headers.items():
          request_object.add_header(key,value)

        if data != None:
          data = urllib.urlencode(data)

        response = urllib2.urlopen(request_object, data)
        return response.read()
