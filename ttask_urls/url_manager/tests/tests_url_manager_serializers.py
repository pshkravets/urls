from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from url_manager.models import RedirectRule
from url_manager.api.serializers import RedirectRuleSerializer


class RedirectRuleSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.redirect_rule = RedirectRule.objects.create(
            redirect_url='https://www.youtube.com/', is_private=True, author=self.user
        )
        self.serializer = RedirectRuleSerializer(instance=self.redirect_rule)

    def test_serializer_contains_correct_fields(self):
        data = self.serializer.data
        expected_keys = ['is_private', 'redirect_url', 'modified_at', 'created_at', 'redirect_identifier', 'id']
        self.assertEqual(list(data.keys()), expected_keys)
