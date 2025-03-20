from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from url_manager.models import RedirectRule


class PublicRedirectView(APIView):

    def get(self, request, redirect_identifier):
        redirect_rule = get_object_or_404(
            RedirectRule,
            redirect_identifier=redirect_identifier,
            is_private=False
        )
        return Response(
            status=status.HTTP_302_FOUND,
            headers={"Location": redirect_rule.redirect_url}
        )


class PrivateRedirectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, redirect_identifier):
        redirect_rule = get_object_or_404(
            RedirectRule,
            redirect_identifier=redirect_identifier,
            is_private=True
        )
        return Response(
            status=status.HTTP_302_FOUND,
            headers={"Location": redirect_rule.redirect_url}
        )
