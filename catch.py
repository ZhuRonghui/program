import requests

r = requests.get('https://www.icourse163.org/learn/NJU-1001571005?tid=1460583445#/learn/content?type=detail&id=1237139226')

print(r.status_code)

print(r.text)

