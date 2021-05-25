import requests
from urllib3.exceptions import InsecureRequestWarning
import warnings

from environment import *


warnings.simplefilter('ignore', InsecureRequestWarning)

class DexcomClarityAPI(object):
    def __init__(self, context):
        print("New  API created")
        self.user = config_data["users"]["demo"]
        self.password = config_data['passwords'][self.user]
        self.data = {
            "username": self.user, 
            "password": self.password,
        }
        self.session = requests.session()
        self.BASE_URL = config_data["environment"]["base_protocol"]
        self.HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
        self.token = None

    def _rest_get(self, context, call):
        href = self.BASE_URL + call
        print(f"Executing API Get: {href}")
        
        response = self.session.get(href, auth=(self.user, self.password), verify=False)
        self.token = response.cookies['idsrv.xsrf']
        assert response.status_code == 200, f"Call to API returned an error: {response.status_code} {response.reason}"
        return response


    def _rest_post(self, context, call):
        href = self.BASE_URL + call
        print(f"Executing API Get: {href}")
        response = self.session.post(href, data={"idsrv.xsrf": self.token})
        print("POSTCOOKIES:" , response.cookies)
        assert response.status_code == 200, f"Call to API returned an error: {response.status_code} {response.content}"
        return response


