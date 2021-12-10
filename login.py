import requests
import json

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

print(response.text)
