import os


class AutoTestConfig(object):

    def __init__(self):
        if os.getenv("AUTOENV") == "DEV":
            self.config_dict = {
                "host": "http://127.0.0.1:8001",
                "user": "admin",
                "pwd": "admin"
            }
        else:
            self.config_dict = {
                "host": "http://192.168.88.28:8000",
                "user": "admin",
                "pwd": "admin",
                "expire_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjMzMTkzNTE0LCJlbWFpbCI6IiJ9.Bh6l3pqqXRz7P4jddNVLb5KcliIJVJUc8HExtvH9kok"
            }

    def get_config(self, key):
        return self.config_dict.get(key)