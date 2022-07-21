import requests
import getpass

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

auth_endpoint = 'http://localhost:8000/api/reader/api-token-auth/'
auth_response = requests.post(auth_endpoint, data={'username': username, 'password': password})

print(auth_response.json())

if auth_response.status_code == 200:
    print('Successfully logged in')

    first_name = input('Enter first name(Press ENTER to keep the previous value): ')
    last_name = input('Enter last name(Press ENTER to keep the previous value): ')
    email = input('Enter email(Press ENTER to keep the previous value): ')
    password = getpass.getpass('Enter password(Press ENTER to keep the previous value): ')
    photo_url = input('Enter photo url(Press ENTER to keep the previous value): ')
    bio = input('Enter bio(Press ENTER to keep the previous value): ')

    token = auth_response.json()['token']
    headers = {'Authorization': 'Token ' + token}
    reader_list_endpoint = 'http://localhost:8000/api/reader/update/'
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'photo_url': photo_url,
        'bio': bio
    }
    detail_response = requests.post(reader_list_endpoint, headers=headers, data=data)
    print(detail_response.json())