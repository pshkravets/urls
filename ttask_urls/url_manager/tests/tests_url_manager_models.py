from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from url_manager.models import RedirectRule


class RedirectRuleModelTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.redirect_rule = RedirectRule.objects.create(
            redirect_url='https://www.youtube.com/', is_private=True, author=self.user
        )

    def test_redirect_rule_creation(self):
        self.assertIsNotNone(self.redirect_rule.redirect_identifier)
        self.assertEqual(self.redirect_rule.author, self.user)
