import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestGenreAPIViewEndpoints:

    endpoint = '/api/genre/'

    def test_list(self, api_client, reader_apiauth_token):
        list_endpoint = f'{self.endpoint}list/'
        list_response = api_client.get(list_endpoint, HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        assert list_response.status_code == 200
         

    def test_create(self, api_client, admin_reader_apiauth_token):
        baked_genre = baker.prepare('genre.Genre')
        genre_data = {
            'name': baked_genre.name
        }
        create_endpoint = f'{self.endpoint}create/'
        create_response = api_client.post(create_endpoint, data = genre_data, format = 'json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert create_response.status_code == 201
        
        
