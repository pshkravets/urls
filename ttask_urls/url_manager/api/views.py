from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import RedirectRuleSerializer
from url_manager.permissions import IsAuthorToDelete
from url_manager.models import RedirectRule


class UrlManagerViewSet(viewsets.ModelViewSet):
    queryset = RedirectRule.objects.all()
    serializer_class = RedirectRuleSerializer
    permission_classes = [IsAuthenticated, IsAuthorToDelete]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer: RedirectRuleSerializer) -> None:
        serializer.save(author=self.request.user)
