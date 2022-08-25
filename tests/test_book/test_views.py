import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestBookAPIViewEndpoints:

    endpoint = '/api/book/'

    @pytest.mark.parametrize('test_param_id',[1, 2])
    def test_list(self, api_client, test_param_id, registered_reader):
        baked_books = baker.make('book.Book', _quantity=1)
        print(baked_books)
        if test_param_id == 1:
            query_data = {
                'isbn': baked_books[0].isbn,
                'title': baked_books[0].title,
                'gte_page_count': baked_books[0].page_count,
                'lte_page_count': baked_books[0].page_count,
                'genre_ids': [1],
                'author_ids': baked_books[0].authors.all(),
            }
        else:
            query_data = {}
        print(f'query_data:\n{query_data}')
        list_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + registered_reader['token'], data=query_data)
        print(list_response.data)
        assert list_response.status_code == 200
        assert 1 == 2

    def test_create(self, api_client, admin_reader_apiauth_token):
        baked_book = baker.prepare('book.Book', page_count = 2677)
        data = {
            'isbn': baked_book.isbn,
            'title': baked_book.title,
            'description': baked_book.description,
            'photo_url': baked_book.photo_url,
            'page_count': baked_book.page_count,
            'genres': baked_book.genres.all(),
            'authors': baked_book.authors.all(),
        }
        print(data)
        create_response = api_client.post(self.endpoint + 'create/', data = data, format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert create_response.status_code == 201

    def test_full_update(self, api_client, admin_reader_apiauth_token):
        baker.make('book.Book')
        baked_book = baker.prepare('book.Book', page_count = 2677)
        data = {
            'isbn': baked_book.isbn,
            'title': baked_book.title,
            'description': baked_book.description,
            'photo_url': baked_book.photo_url,
            'page_count': baked_book.page_count,
            'genres': baked_book.genres.all(),
            'authors': baked_book.authors.all(),
        }
        lis_response = api_client.get(self.endpoint + 'list/')
        endpoint = self.endpoint + 'update/' + lis_response.data[0]['isbn'] + '/'
        update_response = api_client.put(endpoint, data = data, format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert update_response.status_code == 200

    @pytest.mark.parametrize('field', ['isbn', 'title', 'description', 'photo_url', 'page_count', 'genres', 'authors'])
    def test_partial_update(self, api_client, admin_reader_apiauth_token, field):
        baker.make('book.Book')
        baked_book = baker.prepare('book.Book', page_count = 2677)
        lis_response = api_client.get(self.endpoint + 'list/')
        endpoint = self.endpoint + 'update/' + lis_response.data[0]['isbn'] + '/'
        if field in ['genres', 'authors']:
            data = {
                field: baked_book.__getattribute__(field).all()
            }
        else:
            data = {
                field: baked_book.__getattribute__(field)
            }
        print(data)
        update_response = api_client.patch(endpoint, data = data, format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert update_response.status_code == 200

    def test_detail(self, api_client):
        baker.make('book.Book')
        lis_response = api_client.get(self.endpoint + 'list/')
        endpoint = self.endpoint + 'detail/' + lis_response.data[0]['isbn'] + '/'
        detail_response = api_client.get(endpoint)
        assert detail_response.status_code == 200

    def test_delete(self, api_client, admin_reader_apiauth_token):
        baker.make('book.Book')
        lis_response = api_client.get(self.endpoint + 'list/')
        endpoint = self.endpoint + 'delete/' + lis_response.data[0]['isbn'] + '/'
        del_response = api_client.delete(endpoint, HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert del_response.status_code == 204

