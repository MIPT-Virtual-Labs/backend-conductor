#!/usr/bin/env python


import requests

url = "http://127.0.0.1:5000/solver/dummy"
request_json = {"function": "factorial", "x": 4}

response = requests.post(url, json=request_json)

status_code = response.status_code
response_json = response.json()

if status_code != 200:
    print(status_code)
else:
    print(response_json)
