import requests
import getpass

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

auth_endpoint = 'http://localhost:8000/api/reader/api-token-auth/'
auth_response = requests.post(auth_endpoint, data={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    print('Successfully logged in')
    
    token = auth_response.json()['token']
    headers = {'Authorization': 'Token ' + token}
    reader_list_endpoint = 'http://localhost:8000/api/reader/detail/'
    detail_response = requests.get(reader_list_endpoint, headers=headers)
    print(detail_response.json())