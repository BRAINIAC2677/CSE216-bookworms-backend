import requests

endpoint = 'https://bookworms-backend77.herokuapp.com/api/reader/api-token-auth/'

data = {
    'username': 'a',
    'password': 'a'
}

response = requests.post(endpoint, data=data)
print(response.json())
print(response.status_code)