from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


# Create your tests here.
class RegistrationLoginAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')

        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'abu',
            'last_name': 'rakib'
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.user_data['email'])

    def test_user_login(self):
        # Register the user first
        self.client.post(self.register_url, self.user_data)

        # Try to login with correct credentials
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        # Try to login with incorrect credentials
        incorrect_login_data = {
            'email': self.user_data['email'],
            'password': 'incorrectpassword'
        }
        response = self.client.post(self.login_url, incorrect_login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
