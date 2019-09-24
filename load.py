import requests
from time import sleep
last_time = 0

while True:
    response = requests.get('http://localhost:5000/load', json={'after': last_time})
    for message in response.json()['messages']:
        print(message)
        last_time = message['time']
    sleep(1)