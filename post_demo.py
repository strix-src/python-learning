import requests
url='https://httpbin.org/post'
my_payload={
        'question':'什么是RAG',
        'temperature':0.7
        }
response=requests.post(url,json=my_payload)
print(response.json()['json'])
