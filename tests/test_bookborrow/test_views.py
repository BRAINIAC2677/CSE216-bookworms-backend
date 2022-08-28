import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestBookBorrowAPIViewEndpoints:

    endpoint = '/api/bookborrow/'

    def test_list(self, api_client, admin_reader_apiauth_token):
        baked_bookborrow = baker.make('bookborrow.BookBorrow')
        print(baked_bookborrow)
        list_response = api_client.get(self.endpoint + 'list/', format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        print(list_response.data)
        assert list_response.status_code == 200

    @pytest.mark.parametrize('test_param_id', [1, 2, 3, 4])
    def test_querylist(self, api_client, test_param_id, registered_reader):
        baked_bookborrow = baker.make('bookborrow.BookBorrow')
        print(baked_bookborrow)
        if test_param_id == 1:
            query_data = {
                'rid': registered_reader['rid'],
            }
        elif test_param_id == 2:
            query_data = {
                'lid': baked_bookborrow.borrowed_from.lid,
            }
        elif test_param_id == 3:
            query_data = {
                'rid': baked_bookborrow.borrowed_by.rid,
                'lid': baked_bookborrow.borrowed_from.lid,
            }
        elif test_param_id == 4:
            query_data = {}
            
        list_response = api_client.get(self.endpoint + 'list/', format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'], data=query_data)
        print(list_response.data)
        assert list_response.status_code == 200
        


    def test_create(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        baked_library = baker.make('library.Library')
        print(baked_book)
        print(baked_library)
        create_data = {
            'book': baked_book.bid,
            'borrowed_from': baked_library.lid,
            'borrowed_by': registered_reader['rid'],
            'returned_date': '2030-01-01',
            'fee': 10.00,
        }
        create_response = api_client.post(self.endpoint + 'create/', create_data, format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])
        print(create_response.data)
        assert create_response.status_code == 201

    def test_delete(self, api_client, registered_reader, registered_library):
        baked_book = baker.make('book.Book')
        print(baked_book)
        create_data = {
            'book': baked_book.bid,
            'borrowed_from': registered_library['lid'],
            'borrowed_by': registered_reader['rid'],
            'returned_date': '2030-01-01',
            'fee': 10.00,
        }
        create_response = api_client.post(self.endpoint + 'create/', create_data, format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])
        print(create_response.data)
        delete_response = api_client.delete(self.endpoint + 'delete/' + str(create_response.data['bbid']) + '/', format='json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(delete_response)
        assert delete_response.status_code == 204