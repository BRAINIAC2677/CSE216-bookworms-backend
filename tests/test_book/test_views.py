from cgi import test
import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestBookAPIViewEndpoints:

    endpoint = '/api/book/'

    @pytest.mark.parametrize('test_param_id',[x for x in range(1,22)])
    def test_list(self, api_client, test_param_id, registered_reader):
        baked_books = baker.make('book.Book', _quantity=1)
        print(baked_books)

        id = baked_books[0].id
        title = baked_books[0].title
        gte_page_count = baked_books[0].page_count
        lte_page_count = baked_books[0].page_count
        genre_ids = baked_books[0].genres.all()
        author_ids = baked_books[0].authors.all()

        if test_param_id == 1:
            query_data = {
                'id': id, 
                'title': title, 
                'gte_page_count': gte_page_count, 
                'lte_page_count': lte_page_count, 
                'genre_ids': genre_ids, 
                'author_ids': author_ids, 
            }
        elif test_param_id == 2:
            query_data = {
                'id': id,
                'title': title,
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
            }
        elif test_param_id == 3:
            query_data = {
                'id': id,
                'title': title,
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
            }
        elif test_param_id == 4:
            query_data = {
                'id': id,
                'title': title,
                'gte_page_count': gte_page_count,
            }
        elif test_param_id == 5:
            query_data = {
                'id': id,
                'title': title,
            }
        elif test_param_id == 6:
            query_data = {
                'id': id,
            }
        elif test_param_id == 7:
            query_data = {
                'title': title,
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
                'author_ids': author_ids,
            }
        elif test_param_id == 8:
            query_data = {
                'title': title,
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
            }
        elif test_param_id == 9:
            query_data = {
                'title': title,
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
            }
        elif test_param_id == 10:
            query_data = {
                'title': title,
                'gte_page_count': gte_page_count,
            }
        elif test_param_id == 11:
            query_data = {
                'title': title,
            }
        elif test_param_id == 12:
            query_data = {
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
                'author_ids': author_ids,
            }
        elif test_param_id == 13:
            query_data = {
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
            }
        elif test_param_id == 14:
            query_data = {
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
            }
        elif test_param_id == 15:
            query_data = {
                'gte_page_count': gte_page_count,
            }
        elif test_param_id == 16:
            query_data = {
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
                'author_ids': author_ids,
            }
        elif test_param_id == 17:
            query_data = {
                'lte_page_count': lte_page_count,
                'genre_ids': genre_ids,
            }
        elif test_param_id == 18:
            query_data = {
                'lte_page_count': lte_page_count,
            }
        elif test_param_id == 19:
            query_data = {
                'genre_ids': genre_ids,
                'author_ids': author_ids,
            }
        elif test_param_id == 20:
            query_data = {
                'genre_ids': genre_ids,
            }
        elif test_param_id == 21:
            query_data = {
                'author_ids': author_ids,
            }
        else:
            query_data = {}
        print(f'query_data:\n{query_data}')
        list_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + registered_reader['token'], data=query_data)
        print(list_response.data)
        assert list_response.status_code == 200

    def test_create(self, api_client, admin_reader_apiauth_token):
        baked_book = baker.prepare('book.Book', page_count = 2677)
        data = {
            'id': baked_book.id,
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
            'id': baked_book.id,
            'title': baked_book.title,
            'description': baked_book.description,
            'photo_url': baked_book.photo_url,
            'page_count': baked_book.page_count,
            'genres': baked_book.genres.all(),
            'authors': baked_book.authors.all(),
        }
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        endpoint = self.endpoint + 'update/' + lis_response.data[0]['id'] + '/'
        update_response = api_client.put(endpoint, data = data, format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert update_response.status_code == 200

    @pytest.mark.parametrize('field', ['id', 'title', 'description', 'photo_url', 'page_count', 'genres', 'authors'])
    def test_partial_update(self, api_client, admin_reader_apiauth_token, field):
        baker.make('book.Book')
        baked_book = baker.prepare('book.Book', page_count = 2677)
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        endpoint = self.endpoint + 'update/' + lis_response.data[0]['id'] + '/'
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

    def test_detail(self, api_client, registered_reader):
        baker.make('book.Book')
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])
        endpoint = self.endpoint + 'detail/' + lis_response.data[0]['id'] + '/'
        detail_response = api_client.get(endpoint)
        assert detail_response.status_code == 200

    def test_delete(self, api_client, admin_reader_apiauth_token):
        baker.make('book.Book')
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        endpoint = self.endpoint + 'delete/' + lis_response.data[0]['id'] + '/'
        del_response = api_client.delete(endpoint, HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert del_response.status_code == 204

