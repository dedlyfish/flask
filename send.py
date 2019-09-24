import requests

response = requests.get('http://127.0.0.1:5000/ping')
print(response.json())

response = requests.post('http://127.0.0.1:5000/send', json={'username':'fish', 'password':'123','text':'some text'})
print(response.json())