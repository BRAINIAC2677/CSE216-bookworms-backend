import pytest 
from model_bakery import baker

pytestmark = pytest.mark.django_db

class TestReaderEndpoints:

    endpoint = '/api/reader/'

    def test_register(self, api_client):
        baked_reader = baker.prepare('reader.Reader', user__email='pytestreader@gmail.com')
        data = {
            'user':{
                'username': baked_reader.user.username,
                'first_name': baked_reader.user.first_name,
                'last_name': baked_reader.user.last_name,
                'email': baked_reader.user.email,
                'password': baked_reader.user.password,
            }
        }
        response = api_client.post(self.endpoint + 'register/', data = data, format = 'json')
        assert response.status_code == 201

    def test_detail(self, api_client, reader_apiauth_token):
        detail_response = api_client.get(self.endpoint + 'detail/', HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        assert detail_response.status_code == 200

    def test_full_update(self, api_client, reader_apiauth_token):
        baked_reader = baker.prepare('reader.Reader', user__email='pytestreader@gmail.com')
        data = {
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
        update_response = api_client.put(self.endpoint + 'update/', data = data, HTTP_AUTHORIZATION='Token ' + reader_apiauth_token, format = 'json')
        assert update_response.status_code == 200

    @pytest.mark.parametrize('field', ['username', 'first_name', 'last_name', 'email', 'password'])
    def test_partial_update(self, api_client, reader_apiauth_token, field):
        baked_reader = baker.prepare('reader.Reader', user__email='pytestreader@gmail.com')
        data = {
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
        update_response = api_client.patch(self.endpoint + 'update/', data = data, HTTP_AUTHORIZATION='Token ' + reader_apiauth_token, format = 'json')
        assert update_response.status_code == 200

    def test_delete(self, api_client, reader_apiauth_token):
        delete_response = api_client.delete(self.endpoint + 'delete/', HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        assert delete_response.status_code == 204
