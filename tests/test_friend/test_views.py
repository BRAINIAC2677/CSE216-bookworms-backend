import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestFriendAPIViewEndpoints:

    endpoint = '/api/friend/'

    pytest.mark.parametrize('test_param_id', [])
    def test_list(self, api_client):
        pass 

    def test_pending_list(self, api_client):
        pass

    def test_create(self, api_client, registered_reader):
        # friendship with ownself. todo: fix this
        create_data = {
            'friendship_from': registered_reader['rid'],
            'friendship_to': registered_reader['rid'],
        }
        create_response = api_client.post(self.endpoint + "create/", create_data, format='json', HTTP_AUTHORIZATION='Token ' +  registered_reader['token'])
        print(f'create_response.data:\n{create_response.data}')
        assert create_response.status_code == 201

    def test_update(self, api_client):
        pass 

    def test_delete(self, api_client):
        pass