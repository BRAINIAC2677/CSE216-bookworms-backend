import requests 
import json

endpoint = 'https://bookworms-back.herokuapp.com/api/api-token-auth/'

username = 'tagore'
password = '123'

response = requests.post(endpoint, data={'username': username, 'password': password})

print(response.status_code)
print(response.json())