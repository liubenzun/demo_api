import requests


class RequestHandler(object):

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"jwt {object}",
        }

    def request_post(self, url, headers=None, params=None, data=None, json=None):
        if headers:
            self.headers.update(headers)

        resp = requests.post(url=url, headers=self.headers, data=data, json=json)
        assert resp.status_code == 200
        print(resp.status_code)
        return resp.json()

    def request_get(self, url, headers=None):
        if headers:
            self.headers.update(headers)

        resp = requests.get(url=url, headers=self.headers)
        print(resp.status_code)
        assert resp.status_code == 200

        return resp.json()
