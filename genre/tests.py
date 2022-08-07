from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class GenreAPIViewTests(TestCase):
    def test_list_genre(self):
        data = {
            'user': {
                'username': 'test1',
                'email': 'test@gmail.com',
                'password': 'pass1',
                'first_name': 'a',
                'last_name': 'b'
            },
            'photo_url': '',
            'bio': ''
        }
        response = self.client.post(
            reverse('reader-register'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = {
            'username': 'test1',
            'password': 'pass1',
        }
        auth_response = self.client.post(
            reverse('api-token-auth'), data, content_type='application/json')
        self.assertEqual(auth_response.status_code, 200)
        token = auth_response.json()['token']
        headers = {'Authorization': 'Token ' + token}
        self.client.get(reverse('genre-list'), **headers)