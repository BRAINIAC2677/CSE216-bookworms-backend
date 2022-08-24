import pytest
from model_bakery import baker  
from rest_framework.test import APIClient

from django.contrib.auth.models import User 


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
            'email': 'pytestreader@gmail.com',
            'password': 'pytest',
        }
    }
    response = api_client.post('/api/reader/register/', data = data, format='json')
    data = {
        'username': 'pytestreader',
        'password': 'pytest'
    }
    response = api_client.post('/api/api-token-auth/', data = data, format='json')
    yield response.data['token']
    api_client.delete('/api/reader/delete/', HTTP_AUTHORIZATION='Token ' + response.data['token'])

@pytest.fixture
def registered_reader(api_client):
    baked_reader = baker.prepare('reader.Reader', user__email='pytest-reg-reader@gmail.com')
    reg_data = {
        'user':{
            'username': baked_reader.user.username,
            'first_name': baked_reader.user.first_name,
            'last_name': baked_reader.user.last_name,
            'email': baked_reader.user.email,
            'password': baked_reader.user.password,
        },
        'bio': baked_reader.bio,
        'photo_url': baked_reader.photo_url,
    }
    reg_endpoint = '/api/reader/register/'
    reg_response = api_client.post(reg_endpoint, data = reg_data, format = 'json')
    reg_data['rid'] = reg_response.data['rid']
    token_data = {
        'username': reg_data['user']['username'],
        'password': reg_data['user']['password']
    }
    token_response = api_client.post('/api/api-token-auth/', data = token_data, format = 'json')
    reg_data['token'] = token_response.data['token']
    yield reg_data
    api_client.delete('/api/reader/delete/', HTTP_AUTHORIZATION='Token ' + reg_data['token'])
    

@pytest.fixture
def library_apiauth_token(api_client):
    baked_library = baker.prepare('library.Library', user__email='pytestlibrary@gmail.com')
    data = {
        'user':{
            'username': baked_library.user.username,
            'email': baked_library.user.email,
            'password': baked_library.user.password,
        },
        'library_name': baked_library.library_name,
        'photo_url': baked_library.photo_url,
        'longitude': baked_library.longitude,
        'latitude': baked_library.latitude
    }
    response = api_client.post('/api/library/register/', data = data, format='json')
    data = {
        'username': baked_library.user.username,
        'password': baked_library.user.password
    }
    response = api_client.post('/api/api-token-auth/', data = data, format='json')
    yield response.data['token']
    api_client.delete('/api/library/delete/', HTTP_AUTHORIZATION='Token ' + response.data['token'])

@pytest.fixture
def admin_reader_apiauth_token(api_client):
    data = {
        'user':{
            'username': 'pytestadmin-reader',
            'first_name': 'pytest',
            'last_name': 'admin-reader',
            'email': 'pytestadmin-reader@gmail.com',
            'password': 'pytest',
        }
    }
    response = api_client.post('/api/reader/register/', data = data, format='json')
    user = User.objects.get(username='pytestadmin-reader')
    user.is_staff = True
    user.save()
    
    data = {
        'username': 'pytestadmin-reader',
        'password': 'pytest'
    }
    response = api_client.post('/api/api-token-auth/', data = data, format='json')
    yield response.data['token']
    api_client.delete('/api/reader/delete/', HTTP_AUTHORIZATION='Token ' + response.data['token'])