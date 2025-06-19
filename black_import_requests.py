# -----------introduction to request-opendir---
# import request use for web application exploitation=---


import requests

x = requests.get('http://httpbin.org/get')

print(x.headers)
print(x.headers['Server'])
print(x.status_code)

if x.status_code == 200:
    print("Sucess!")
elif x.status_code == 404:
    print("Not found")

print(x.elapsed)
print(x.cookies)
print(x.text)