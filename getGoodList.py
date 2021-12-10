import requests

url = "http://127.0.0.1:8000/goods/"

payload={}
headers = {
  'Authorization': 'jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjM5MDQxMDM4LCJlbWFpbCI6IiJ9.dym1xBa3g716EfH-TWh7niqI-1ERaw2VIAc6QgL--sQ',
  'Cookie': 'sessionid=d92d967enkjt0ya5e9h15qi2m6hougbb'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
