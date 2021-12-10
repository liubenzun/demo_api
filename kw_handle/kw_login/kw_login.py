import json

from lib.requestHandle import RequestHandler


def kw_login_getToken(username, password):
    request_handelClass = RequestHandler();
    url = "http://127.0.0.1:8000/login/"

    payload = json.dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
    }

    response = request_handelClass.request_post(url=url, headers=headers, data=payload)
    return response["data"]["token"]
