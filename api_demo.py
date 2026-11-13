import requests
url="https://api.github.com/users/torvalds"
reponse=requests.get(url,timeout=10)
if reponse.status_code==200:
    data=reponse.json()
    print(f"name is {data.get('name')},followers is {data.get('followers')}")
else:
    print(f"error is {reponse.status_code}")
