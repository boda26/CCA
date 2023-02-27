import requests
import json

payload = {
        "USE_CACHE": "True",
        "REQUEST": "read",
        "SQLS": [1,2,3]
    }
api = "https://avkyr7vqoj.execute-api.us-east-1.amazonaws.com/stage2"
r = requests.post(api, data=json.dumps(payload))
print(r)
res = ""
res = r.json()['body']
