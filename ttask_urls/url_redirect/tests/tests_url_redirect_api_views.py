from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from url_manager.models import RedirectRule


class RedirectViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.public_redirect = RedirectRule.objects.create(
            redirect_url='https://example.com/public', is_private=False, author=self.user
        )
        self.private_redirect = RedirectRule.objects.create(
            redirect_url='https://example.com/private', is_private=True, author=self.user
        )

    def test_public_redirect_found(self):
        url = reverse('public-url-redirect-api', args=[self.public_redirect.redirect_identifier])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.headers['Location'], self.public_redirect.redirect_url)

    def test_public_redirect_not_found(self):
        url = reverse('public-url-redirect-api', args=['nonexistent'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_private_redirect_authenticated(self):
        url = reverse('private-url-redirect-api', args=[self.private_redirect.redirect_identifier])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.headers['Location'], self.private_redirect.redirect_url)

    def test_private_redirect_not_found(self):
        url = reverse('private-url-redirect-api', args=['nonexistent'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_private_redirect_unauthorized(self):
        self.client.credentials()
        url = reverse('private-url-redirect-api', args=[self.private_redirect.redirect_identifier])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
