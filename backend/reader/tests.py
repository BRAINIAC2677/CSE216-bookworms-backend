from django.urls import reverse
from django.test import TestCase

# Create your tests here.


class ReaderRegisterAPIViewTests(TestCase):
    def test_register_with_duplicate_email(self):
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
            'user': {
                'username': 'test2',
                'email': 'test@gmail.com',
                'password': 'pass2',
                'first_name': 'c',
                'last_name': 'd'
            },
            'photo_url': '',
            'bio': ''
        }
        response = self.client.post(
            reverse('reader-register'), data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


class ReaderTokenAuthenticationTests(TestCase):
    def test_token_authentication(self):
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
            'password': 'pass1'
        }
        response = self.client.post(
            reverse('api-token-auth'), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)


class ReaderUpdateAPIViewTests(TestCase):
    def test_basic_update(self):
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
        data = {}
        self.client.post(reverse('reader-update'), data,
                         content_type='application/json', **headers)
        self.assertEqual(response.status_code, 201)
