import time

import requests
import json
from lib.requestHandle import RequestHandler

from kw_handle.kw_login.kw_login import kw_login_getToken


class TestGoodList:

    def setup(self):
        self.handle = RequestHandler()
        self.token=kw_login_getToken(username="admin",password="admin")


    def test_case1(self):
        url = "http://127.0.0.1:8000/goods/"

        headers = {
            'Authorization': f"jwt {self.token}",
            'Cookie9': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
        }

        response = self.handle.request_get(url=url,headers=headers)

        assert response["code"] == 200

        print(type(response))
