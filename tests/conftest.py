import pytest 
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def reader_apiauth_token(api_client):
    data = {
        'user':{
            'username': 'pytestreader',
            'first_name': 'pytest',
            'last_name': 'reader',
            'email': 'test@gmail.com',
            'password': 'pytest',
        }
    }
    response = api_client.post('/api/reader/register/', data = data, format='json')
    data = {
        'username': 'pytestreader',
        'password': 'pytest'
    }
    response = api_client.post('/api/reader/api-token-auth/', data = data, format='json')
    yield response.data['token']
    api_client.delete('/api/reader/delete/', HTTP_AUTHORIZATION='Token ' + response.data['token'])
    