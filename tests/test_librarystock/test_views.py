import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestLibraryStockAPIViewEndpoints:

    endpoint = '/api/librarystock/'

    @pytest.mark.parametrize('test_param_id', [1, 2])
    def test_list(self, api_client, registered_library, test_param_id):
        baked_librarystock = baker.make('librarystock.LibraryStock')
        print(f'baked_librarystock:\n{baked_librarystock}')
        if test_param_id == 1:
            query_data = {
                'lid': baked_librarystock.library.lid
            }
        else:
            query_data = {}
        print(f'query_data:\n{query_data}')
        list_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + registered_library['token'], data = query_data)
        print(f'list_response.data:\n{list_response.data}')
        assert list_response.status_code == 200

    def test_detail(self, api_client, registered_library):
        baked_book = baker.make('book.Book')
        print(baked_book)
        create_data = {
            'book': baked_book.bid,
            'library': registered_library['lid'],
            'quantity': -1,  
            'borrow_fee_per_day': 10
        }
        create_response = api_client.post(self.endpoint + 'create/', data = create_data, format = 'json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(create_response.data)
        detail_response = api_client.get(self.endpoint + 'detail/' + str(create_response.data['lsid']) + '/', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(detail_response.data)
        assert detail_response.status_code == 200

    # todo: one library is creating librarystock for another library which is not expected.
    def test_create(self, api_client, library_apiauth_token):
        baked_book = baker.make('book.Book')
        baked_library = baker.make('library.Library')
        create_data = {
            'book': baked_book.bid,
            'library': baked_library.lid,
            'quantity': -1,  
            'borrow_fee_per_day': 10
        }
        create_response = api_client.post(self.endpoint + 'create/', data = create_data, format = 'json', HTTP_AUTHORIZATION='Token ' + library_apiauth_token)
        print(create_response.data)
        assert create_response.status_code == 201

    def test_full_update(self, api_client, registered_library):
        baked_book = baker.make('book.Book')
        print(baked_book)
        create_data = {
            'book': baked_book.bid,
            'library': registered_library['lid'],
            'quantity': -1,  
            'borrow_fee_per_day': 10
        }
        create_response = api_client.post(self.endpoint + 'create/', data = create_data, format = 'json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(create_response.data)
        upd_data = {
            'quantity': 10,
            'borrow_fee_per_day': 13
        }
        upd_response = api_client.put(self.endpoint + 'update/' + str(create_response.data['lsid']) + '/', data = upd_data, format = 'json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(upd_response.data)
        assert upd_response.status_code == 200

    @pytest.mark.parametrize('field', ['quantity', 'borrow_fee_per_day'])
    def test_partial_update(self, api_client, field, registered_library):
        baked_book = baker.make('book.Book')
        print(baked_book)
        create_data = {
            'book': baked_book.bid,
            'library': registered_library['lid'],
            'quantity': -1,  
            'borrow_fee_per_day': 10
        }
        create_response = api_client.post(self.endpoint + 'create/', data = create_data, format = 'json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(create_response.data)
        if field == 'quantity':
            upd_data = {
                'quantity': 10
            } 
        elif field == 'borrow_fee_per_day':
            upd_data = {
                'borrow_fee_per_day': 13
            }
        upd_response = api_client.patch(self.endpoint + 'update/' + str(create_response.data['lsid']) + '/', data = upd_data, format = 'json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(upd_response.data)
        assert upd_response.status_code == 200

    def test_delete(self, api_client, registered_library):
        baked_book = baker.make('book.Book')
        print(baked_book)
        create_data = {
            'book': baked_book.bid,
            'library': registered_library['lid'],
            'quantity': -1,  
            'borrow_fee_per_day': 10
        }
        create_response = api_client.post(self.endpoint + 'create/', data = create_data, format = 'json', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
        print(create_response.data)
        delete_response = api_client.delete(self.endpoint + 'delete/' + str(create_response.data['lsid']) + '/', HTTP_AUTHORIZATION='Token ' + registered_library['token'])
 

