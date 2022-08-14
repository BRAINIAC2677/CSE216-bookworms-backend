from urllib import response
import requests
import json



# data = {
#     'user':{
#         'username': 'b',
#         'first_name': 'b',
#         'last_name': 'b',
#         'email': 'b@gmail.com',
#         'password': 'b'
#     }
# }
# endpoint = 'http://127.0.0.1:8000/api/reader/register/'
# response = requests.post(endpoint, json = data)
# print(response.status_code)

endpoint = 'http://127.0.0.1:8000/api/reader/api-token-auth/'

data = {
    'username': 'b',
    'password': 'b'
}

response = requests.post(endpoint, data = data)
print(response.status_code)

token = response.json()['token']
endpoint = 'http://127.0.0.1:8000/api/reader/update/'
data = {
    'user':{}, 
    'bio': 'updated'
}
response = requests.put(endpoint, json = data, headers = {'Authorization': 'Token ' + token})
print(response.status_code)