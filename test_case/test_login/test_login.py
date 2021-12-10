import json

import requests



class TestLogin:
    # 登陆成功
    def test_case1(self):
        url = "http://127.0.0.1:8000/login/"

        payload = json.dumps({
            "username": "admin",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        result = response.json()
        assert response.status_code == 200
        assert result["code"] == 200
        assert result["message"] == "登录成功"
        assert result["data"]["token"]

    def test_case2(self):
        url = "http://127.0.0.1:8000/login/"

        payload = json.dumps({
            "username": "admin1",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        result = response.json()
        assert response.status_code == 200
        assert result["code"] == 500
        assert result["message"] == "账号或密码错误"

    def test_case3(self):
        # 登陆请求踢缺少参数
        url = "http://127.0.0.1:8000/login/"

        payload = json.dumps({
            "username": "admin1",

        })
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        result = response.json()
        assert response.status_code == 200
        assert result["code"] == 500
        assert result["message"] == "请求参数错误"
