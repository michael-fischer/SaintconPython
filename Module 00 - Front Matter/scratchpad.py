import requests

request = requests.get('https://www.google.com/')
if request.status_code == 200:
        print(request.content) 