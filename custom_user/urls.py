from django.conf.urls import url, include
from rest_framework import routers

from custom_user.views import CustomUsersViewSet


router = routers.DefaultRouter()
router.register(r'users', CustomUsersViewSet, base_name='users_view')


urlpatterns = [
    url(r'', include(router.urls)),
]
