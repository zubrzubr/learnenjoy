from django.conf.urls import url, include
from rest_framework import routers

from reward.views import RewardsViewSet


router = routers.DefaultRouter()
router.register(r'rewards', RewardsViewSet, base_name='rewards_view')


urlpatterns = [
    url(r'', include(router.urls)),
]
