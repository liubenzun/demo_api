import time

import requests
import json
from kw_handle.kw_login.kw_login import kw_login_getToken


class TestGoodList:

    def setup(self):
        self.token=kw_login_getToken(username="admin",password="admin")

    def test_case1(self):
        url = "http://127.0.0.1:8000/goods/"
        timestamp = int(time.time())
        payload = json.dumps({
            "name": f"发咖啡{timestamp}",
            "desc": f"阿发福卡{timestamp}设计开发"
        })

        headers = {
            'Authorization': f'jwt {self.token}',
            'Content-Type': 'application/json',
            'Cookie': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        res = response.json()
        assert response.status_code == 200
        assert res["code"] == 200
        assert res["message"] == f"创建商品发咖啡{timestamp}成功"

