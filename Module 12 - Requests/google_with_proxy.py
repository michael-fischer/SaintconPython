import requests

PROXY = True
proxy = {}

if PROXY:
    proxy['http'] = 'http://localhost:8080'
    proxy['https'] = 'https://localhost:8080'

# The following 
request = requests.get('https://www.google.com/', proxies = proxy, verify = '/Users/mfischer/Downloads/certificate.pem')
if request.status_code == 200:
    print('success')