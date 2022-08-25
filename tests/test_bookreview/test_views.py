import pytest 
from model_bakery import baker 

pytestmark = pytest.mark.django_db

class TestBookReviewAPIViewEndpoints:

    endpoint = '/api/bookreview/'

    def test_list(self, api_client):
        baker.make('bookreview.BookReview', _quantity=3)
        lis_response = api_client.get(self.endpoint + 'list/')
        assert lis_response.status_code == 200
        assert len(lis_response.data) == 3

    def test_detail(self, api_client):
        bookreview = baker.make('bookreview.BookReview')
        detail_response = api_client.get(self.endpoint + f'detail/{bookreview.brid}/')
        assert detail_response.status_code == 200
    
    def test_create(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        data = {
            'book': baked_book.id,
            'reviewer': registered_reader['rid'],
            'rating': 5,
            'content': 'This is a test review.',
        }
        create_response = api_client.post(self.endpoint + 'create/', data, format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])
        assert create_response.status_code == 201
        assert create_response.data['rating'] == 5
        assert create_response.data['content'] == 'This is a test review.'
    
    def test_full_update(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        data = {
            'book': baked_book.id,
            'reviewer': registered_reader['rid'],
            'rating': 5,
            'content': 'This is a test review.',
        }
        create_response = api_client.post(self.endpoint + 'create/', data, format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])        
        upd_data = {
            'rating': 4,
            'content': 'This is a updated review.',
        }
        upd_endpoint = f'{self.endpoint}update/{create_response.data["brid"]}/'
        upd_response = api_client.put(upd_endpoint,upd_data, format='json', HTTP_AUTHORIZATION = 'Token ' + registered_reader['token'])
        assert upd_response.status_code == 200
    
    @pytest.mark.parametrize('field', ['rating', 'content'])
    def test_partial_update(self, api_client, registered_reader, field):
        baked_book = baker.make('book.Book')
        data = {
            'book': baked_book.id,
            'reviewer': registered_reader['rid'],
            'rating': 5,
            'content': 'This is a test review.',
        }
        create_response = api_client.post(self.endpoint + 'create/', data, format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])        
        if field == 'rating':
            upd_data = {
                field: 3
            }
        elif field == 'content':
            upd_data = {
                field: 'This is updated review'
            }
        upd_endpoint = f'{self.endpoint}update/{create_response.data["brid"]}/'
        upd_response = api_client.put(upd_endpoint,upd_data, format='json', HTTP_AUTHORIZATION = 'Token ' + registered_reader['token'])
        assert upd_response.status_code == 200

    def test_update_lovedby(self, api_client, registered_reader):
        baked_book = baker.make('book.Book')
        data = {
            'book': baked_book.id,
            'reviewer': registered_reader['rid'],
            'rating': 5,
            'content': 'This is a test review.',
        }
        create_response = api_client.post(self.endpoint + 'create/', data, format='json', HTTP_AUTHORIZATION='Token ' + registered_reader['token'])        
        upd_data = {
            'loved_by': [registered_reader['rid'],],
        }
        upd_endpoint = f'{self.endpoint}update/lovedby/{create_response.data["brid"]}/'
        upd_response = api_client.put(upd_endpoint,upd_data, format='json', HTTP_AUTHORIZATION = 'Token ' + registered_reader['token'])
        assert upd_response.status_code == 200
        
