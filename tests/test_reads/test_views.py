import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestReadsAPIViewEndpoints:

    endpoint = '/api/reads/'

    def test_list(self, api_client, registered_reader):
        baked_read = baker.make('reads.Reads')
        print(baked_read)
        list_response = api_client.get(self.endpoint + 'list/', format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        print(list_response.data)
        assert list_response.status_code == 200

    def test_detail(self, api_client, registered_reader):
        baked_read = baker.make('reads.Reads')
        print(baked_read)
        detail_response = api_client.get(self.endpoint + 'detail/' + str(baked_read.rsid) + '/', format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        print(detail_response.data)
        assert detail_response.status_code == 200

    def test_create(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        create_data = {
            'reader': registered_reader['rid'],
            'book': baked_book.isbn,
            'status': 'w',
        } 
        create_response = api_client.post(self.endpoint + 'create/', create_data, format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        print(create_response.data)
        assert create_response.status_code == 201

    def test_full_update(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        create_data = {
            'reader': registered_reader['rid'],
            'book': baked_book.isbn,
            'status': 'w',
        } 
        create_response = api_client.post(self.endpoint + 'create/', create_data, format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        print(create_response.data)
        upd_data = {
            'status': 'c',
        }
        upd_response = api_client.put(self.endpoint + 'update/' + str(create_response.data['rsid']) + '/', upd_data, format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        print(upd_response.data)
        assert upd_response.status_code == 200 

    def test_delete(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        create_data = {
            'reader': registered_reader['rid'],
            'book': baked_book.isbn,
            'status': 'w',
        } 
        create_response = api_client.post(self.endpoint + 'create/', create_data, format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        print(create_response.data)
        delete_response = api_client.delete(self.endpoint + 'delete/' + str(create_response.data['rsid']) + '/', format='json', HTTP_AUTHORIZATION= 'Token ' + registered_reader['token'])
        assert delete_response.status_code == 204