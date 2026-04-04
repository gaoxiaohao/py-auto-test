import requests
import json as complexjson



class HttpClient:

    def __init__(self,api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.Session()

    def get(self,url,**kwargs):
        return self.request('GET',url,**kwargs)

    def post(self,url,data=None,json=None,**kwargs):
        return self.request('POST',url,data,json,**kwargs)

    def put(self,url,data=None,**kwargs):
        return self.request('PUT',url,data,**kwargs)

    def patch(self,url,data=None,**kwargs):
        return self.request('PATCH',url,data,**kwargs)

    def delete(self,url,**kwargs):
        return self.request('DELETE',url,**kwargs)


    def request(self,method,url,data=None,json=None,**kwargs):
        url = self.api_root_url + url
        if method == "GET":
            return self.session.get(url,**kwargs)
        elif method == "POST":
            return self.session.post(url,data=data,json=json,**kwargs)
        elif method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url,data=data,**kwargs)
        elif method == "DELETE":
            return self.session.delete(url,**kwargs)
        elif method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url,data,**kwargs)
        return None

