import pytest 
from model_bakery import baker

pytestmark = pytest.mark.django_db

class TestReaderAPIViewEndpoints:

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
            },
            'bio': baked_reader.bio,
            'photo_url': baked_reader.photo_url,
        }
        response = api_client.post(self.endpoint + 'register/', data = data, format = 'json')
        assert response.status_code == 201

    def test_list(self, api_client, reader_apiauth_token):
        list_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        assert list_response.status_code == 200

    def test_my_detail(self, api_client, reader_apiauth_token):
        detail_response = api_client.get(self.endpoint + 'my-detail/', HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        assert detail_response.status_code == 200

    def test_detail(self, api_client, reader_apiauth_token):
        baked_reader = baker.prepare('reader.Reader', user__email='r@gmail.com')
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
        reg_response = api_client.post(self.endpoint + 'register/', data = data, format = 'json')
        print(reg_response.json())
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        endpoint = f'{self.endpoint}detail/{lis_response.data[1]["rid"]}/'
        detail_response = api_client.get(endpoint, HTTP_AUTHORIZATION='Token ' + reader_apiauth_token)
        assert detail_response.status_code == 200        

    def test_full_update(self, api_client, reader_apiauth_token):
        baked_reader = baker.prepare('reader.Reader', user__email='upd-pytestreader@gmail.com')
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

    @pytest.mark.parametrize('field', ['username', 'first_name', 'last_name', 'email', 'password', 'bio', 'photo_url'])
    def test_partial_update(self, api_client, reader_apiauth_token, field):
        baked_reader = baker.prepare('reader.Reader', user__email='upd-pytestreader@gmail.com')
        if field in ['username', 'first_name', 'last_name', 'email', 'password']:
            data = {
                'user':{
                    field: baked_reader.user.__getattribute__(field)
                }
            }
        else:
            data = {
                field: baked_reader.__getattribute__(field)
            }
        update_response = api_client.patch(self.endpoint + 'update/', data = data, HTTP_AUTHORIZATION='Token ' + reader_apiauth_token, format = 'json')
        assert update_response.status_code == 200

    def test_delete(self, api_client, registered_reader):
        delete_response = api_client.delete(self.endpoint + 'delete/' + str(registered_reader['rid']) + '/', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])
        assert delete_response.status_code == 204
