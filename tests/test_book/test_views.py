from cgi import test
import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestBookAPIViewEndpoints:

    endpoint = '/api/book/'

    @pytest.mark.parametrize('test_param_id',[x for x in range(12,22)])
    def test_list(self, api_client, test_param_id, registered_reader):
        baked_genre = baker.make('genre.Genre')
        baked_reader = baker.make('reader.Reader')
        baked_book = baker.make('book.Book', page_count = 2677, genres = [baked_genre], authors = [baked_reader])

        print(f'baked_genre:\n{baked_genre}')
        print(f'baked_reader:\n{baked_reader}')
        print(f'baked_book:\n{baked_book}')

        gte_page_count = baked_book.page_count
        lte_page_count = baked_book.page_count
        genre_id = baked_book.genres.all()[0].gid
        author_id = baked_book.authors.all()[0].rid

        if test_param_id == 12:
            query_data = {
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_id': genre_id,
                'author_id': author_id,
            }
        elif test_param_id == 13:
            query_data = {
                'gte_page_count': gte_page_count,
                'lte_page_count': lte_page_count,
                'genre_id': genre_id,
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
                'genre_id': genre_id,
                'author_id': author_id,
            }
        elif test_param_id == 17:
            query_data = {
                'lte_page_count': lte_page_count,
                'genre_id': genre_id,
            }
        elif test_param_id == 18:
            query_data = {
                'lte_page_count': lte_page_count,
            }
        elif test_param_id == 19:
            query_data = {
                'genre_id': genre_id,
                'author_id': author_id,
            }
        elif test_param_id == 20:
            query_data = {
                'genre_id': genre_id,
            }
        elif test_param_id == 21:
            query_data = {
                'author_id': author_id,
            }
        else:
            query_data = {}
        print(f'query_data:\n{query_data}')
        list_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + registered_reader['token'], data=query_data)
        print(list_response.data)
        assert list_response.status_code == 200


    def test_create(self, api_client, admin_reader_apiauth_token):
        baked_book = baker.prepare('book.Book', page_count = 2677)
        create_data = {
            'bid': baked_book.bid,
            'title': baked_book.title,
            'description': baked_book.description,
            'photo_url': baked_book.photo_url,
            'page_count': baked_book.page_count,
            'genres': baked_book.genres.all(),
            'authors': baked_book.authors.all(),
        }
        print(create_data)
        create_response = api_client.post(self.endpoint + 'create/', data = create_data, format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        print(create_response.data)
        assert create_response.status_code == 201

    def test_full_update(self, api_client, admin_reader_apiauth_token):
        baked_book1 = baker.make('book.Book')
        baked_book2 = baker.prepare('book.Book', page_count = 2677)
        data = {
            'bid': baked_book2.bid,
            'title': baked_book2.title,
            'description': baked_book2.description,
            'photo_url': baked_book2.photo_url,
            'page_count': baked_book2.page_count,
            'genres': baked_book2.genres.all(),
            'authors': baked_book2.authors.all(),
        }
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        endpoint = self.endpoint + 'update/' + lis_response.data[0]['bid'] + '/'
        update_response = api_client.put(endpoint, data = data, format='json', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert update_response.status_code == 200

    @pytest.mark.parametrize('field', ['bid', 'title', 'description', 'photo_url', 'page_count', 'genres', 'authors'])
    def test_partial_update(self, api_client, admin_reader_apiauth_token, field):
        baker.make('book.Book')
        baked_book = baker.prepare('book.Book', page_count = 2677)
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        endpoint = self.endpoint + 'update/' + lis_response.data[0]['bid'] + '/'
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
        endpoint = self.endpoint + 'detail/' + lis_response.data[0]['bid'] + '/'
        detail_response = api_client.get(endpoint, HTTP_AUTHORIZATION='Token ' + registered_reader['token'])
        print(detail_response.data)
        assert detail_response.status_code == 200

    def test_delete(self, api_client, admin_reader_apiauth_token):
        baker.make('book.Book')
        lis_response = api_client.get(self.endpoint + 'list/', HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        endpoint = self.endpoint + 'delete/' + lis_response.data[0]['bid'] + '/'
        del_response = api_client.delete(endpoint, HTTP_AUTHORIZATION='Token ' + admin_reader_apiauth_token)
        assert del_response.status_code == 204

