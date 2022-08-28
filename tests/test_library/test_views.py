import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestLibraryAPIViewEndpoints:
    
    endpoint = '/api/library/'

    def test_register(self, api_client):
        baked_library = baker.prepare('library.Library', user__email='pytestlibrary@gmail.com')
        create_data = {
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
        print(f'create_data:\n{create_data}')
        response = api_client.post(self.endpoint + 'register/', data = create_data, format = 'json')
        print(f'response data:\n{response.data}')
        assert response.status_code == 201

    def test_list(self, api_client, library_apiauth_token):
        list_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + library_apiauth_token)
        assert list_response.status_code == 200

    def test_detail(self, api_client, library_apiauth_token):
        baked_library = baker.prepare('library.Library', user__email='l@gmail.com')
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
        api_client.post(self.endpoint + 'register/', data = data, format = 'json')
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + library_apiauth_token)
        endpoint = f'{self.endpoint}detail/{lis_response.data[1]["lid"]}/'
        detail_response = api_client.get(endpoint, HTTP_AUTHORIZATION='Token ' + library_apiauth_token)
        print(detail_response.status_code)
        assert detail_response.status_code == 200

    def test_my_detail(self, api_client, library_apiauth_token):
        detail_response = api_client.get(self.endpoint + 'my-detail/', HTTP_AUTHORIZATION='Token ' + library_apiauth_token)
        assert detail_response.status_code == 200

    def test_full_update(self, api_client, library_apiauth_token):
        baked_library = baker.prepare('library.Library', user__email='upd-pytestlibrary@gmail.com')
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
        upd_response = api_client.put(self.endpoint + 'update/', data = data, HTTP_AUTHORIZATION='Token ' + library_apiauth_token, format = 'json')
        assert upd_response.status_code == 200

    @pytest.mark.parametrize('field', ['username', 'email', 'password', 'library_name', 'photo_url', 'longitude', 'latitude'])
    def test_partial_update(self, api_client, library_apiauth_token, field):
        baked_library = baker.prepare('library.Library', user__email='upd-pytestlibrary@gmail.com')
        if field in ['username', 'email', 'password']:
            data = {
                'user': {
                    field: baked_library.user.__getattribute__(field)
                }
            }
        else:
            data = {
                field: baked_library.__getattribute__(field)
            }
        update_response = api_client.patch(self.endpoint + 'update/', data = data, HTTP_AUTHORIZATION='Token ' + library_apiauth_token, format = 'json')
        assert update_response.status_code == 200

    def test_delete(self, api_client, library_apiauth_token):
        delete_response = api_client.delete(self.endpoint + 'delete/', HTTP_AUTHORIZATION='Token ' + library_apiauth_token)
        assert delete_response.status_code == 204        