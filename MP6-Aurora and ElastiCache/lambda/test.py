import requests
import json

url = 'https://ikm2evu584.execute-api.us-east-1.amazonaws.com/test/mp11-autograder'

payload = {
			"submitterEmail": "boda2@illinois.edu", # <insert your coursera account email>,
			"secret": "31bwAqcvAuZM703H", # <insert your secret token from coursera>,
			# "partId" : "G6U3L"
			"dbApi": "https://avkyr7vqoj.execute-api.us-east-1.amazonaws.com/stage2"
		}
print(json.dumps(payload))
r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)