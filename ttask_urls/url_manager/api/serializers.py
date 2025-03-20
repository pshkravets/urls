from rest_framework import serializers

from url_manager.models import RedirectRule


class RedirectRuleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RedirectRule
        fields = [
            'is_private', 'redirect_url', 'modified_at', 'created_at', 'author', 'redirect_identifier', 'id'
        ]
        read_only_fields = ['created_at', 'modified_at', 'author', 'redirect_identifier', 'id']
