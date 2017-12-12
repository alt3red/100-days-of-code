import requests

json = requests.get('http://httpbin.org/user-agent').json()
print(json['user-agent'])
