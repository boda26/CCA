import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1': '18.191.160.104:5000',  # <insert ip address:port of first EC2 instance>, 
		'ip_address2': '13.58.54.178:5000', # <insert ip address:port of secong EC2 instance>,
		'load_balancer': 'lb1-2034865922.us-east-2.elb.amazonaws.com', # <insert address of load balancer>,
		'submitterEmail': 'boda2@illinois.edu',  # <insert your coursera account email>,
		'secret': 'KIU65lmYx0wf1c8U'  # <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)