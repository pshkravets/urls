from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from url_manager.models import RedirectRule


class UrlManagerViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='otheruser', password='password')
        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.redirect_rule = RedirectRule.objects.create(
            redirect_url='https://www.youtube.com/', is_private=True, author=self.user
        )

    def test_list_redirect_rules(self):
        response = self.client.get(reverse('url-manager-api-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_redirect_rule(self):
        data = {'redirect_url': 'https://www.youtube.com/', 'is_private': False}
        response = self.client.post(reverse('url-manager-api-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RedirectRule.objects.count(), 2)

    def test_update_redirect_rule(self):
        data = {'redirect_url': 'https://github.com/', 'is_private': False}
        response = self.client.patch(reverse('url-manager-api-detail', kwargs={'pk': self.redirect_rule.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.redirect_rule.refresh_from_db()
        self.assertEqual(self.redirect_rule.redirect_url, 'https://github.com/')

    def test_delete_redirect_rule(self):
        response = self.client.delete(reverse('url-manager-api-detail', kwargs={'pk': self.redirect_rule.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RedirectRule.objects.count(), 0)

    def test_forbidden_delete_by_other_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {AccessToken.for_user(self.other_user)}')
        response = self.client.delete(reverse('url-manager-api-detail', kwargs={'pk': self.redirect_rule.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
