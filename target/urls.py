from django.conf.urls import url, include
from rest_framework import routers

from target.views import TargetsViewSet


router = routers.DefaultRouter()
router.register(r'targets', TargetsViewSet, base_name='targets')


urlpatterns = [
    url(r'', include(router.urls)),
]
