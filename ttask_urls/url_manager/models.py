import uuid

from django.db import models
from django.contrib.auth.models import User


class RedirectRule(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    redirect_url = models.URLField(null=False)
    is_private = models.BooleanField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    redirect_identifier = models.CharField(max_length=16, unique=True, editable=False)

    def save(self, *args: list, **kwargs: dict) -> None:
        if not self.redirect_identifier:
            self.redirect_identifier = self.generate_unique_identifier()
        super().save(*args, **kwargs)

    def generate_unique_identifier(self) -> str:
        return uuid.uuid4().hex[:16]
