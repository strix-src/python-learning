import requests
url='https://httpbin.org/headers'
my_headers={
        'Authorization':'Bearer ask=1234567890abcdef',
        'Content-Type':'application/json'
        }
response=requests.get(url,headers=my_headers)
print(response.json())
