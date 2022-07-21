import requests
import getpass

# register a new reader
username = input('Enter username(required): ')
first_name = input('Enter first name(required): ')
last_name = input('Enter last name(required): ')
bio = input('Enter bio(Optional.Press ENTER to avoid): ')
photo_url = input('Enter photo url(Optional.Press ENTER to avoid): ')
email = input('Enter email(required): ')
password = getpass.getpass('Enter password(required): ')
confirm_password = getpass.getpass('Confirm password(required): ')

data = {
    'username': username,
    'first_name': first_name,
    'last_name': last_name,
    'bio': bio,
    'photo_url': photo_url,
    'email': email,
    'password': password,
    'confirm_password': confirm_password
}

endpoint = 'http://localhost:8000/api/reader/register/'
response = requests.post(endpoint, data=data)
print(response.json())
