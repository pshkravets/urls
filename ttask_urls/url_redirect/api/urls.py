from django.urls import path

from .views import PrivateRedirectView, PublicRedirectView


urlpatterns = [
    path('public/<str:redirect_identifier>', PublicRedirectView.as_view(), name='public-url-redirect-api'),
    path('private/<str:redirect_identifier>', PrivateRedirectView.as_view(), name='private-url-redirect-api')
]
