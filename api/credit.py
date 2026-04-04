from core.http_client import HttpClient
from pathlib import Path
import configparser

BASE_PATH = Path(__file__).resolve().parent.parent
config = configparser.ConfigParser()
print(BASE_PATH)
config.read(BASE_PATH /'config'/'setting.ini', encoding='utf-8')
api_root_url = config.get("host", "api_root_url")

class Credit(HttpClient):

    def __init__(self):
        super().__init__(api_root_url)
        self.api_root_url = api_root_url


    def apply_credit(self, json,**kwargs):
        return self.post('/credit/apply', json=json,**kwargs)

    def query_credit(self,json=None,**kwargs):
        return self.post('/credit/query',json=json,**kwargs)


credit = Credit()