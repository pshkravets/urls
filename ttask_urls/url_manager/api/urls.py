from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UrlManagerViewSet


router = SimpleRouter()
router.register('', UrlManagerViewSet, basename='url-manager-api')


urlpatterns =[
    path('', include(router.urls))
]
