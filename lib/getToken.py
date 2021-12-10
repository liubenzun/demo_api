import requests


class getTokenClass(object):
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',

        }

    def getTokenFucntion(self, url, headers=None, data=None, json=None):
        respsonse = requests.post(url=url, headers=self.headers, data=data, json=json)
        if headers:
            self.headers.update(headers)

        if respsonse.status_code == 200:
            resp = respsonse.json()
            return resp["data"]["token"]

        if respsonse.status_code != 200:
            resp = respsonse.json()

            return resp
