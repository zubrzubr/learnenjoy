from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


swagger_view = get_swagger_view(title='Learn to enjoy API')

api_v1_pattern = r'^api/v1/'

api_urls = [
    url(api_v1_pattern, include('book.urls')),
    url(api_v1_pattern, include('target.urls')),
    url(api_v1_pattern, include('custom_user.urls')),
    url(api_v1_pattern, include('reward.urls')),
    url('{}{}'.format(api_v1_pattern, 'login/token/$'), TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('{}{}'.format(api_v1_pattern, 'login/token/refresh/$'), TokenRefreshView.as_view(), name='token_refresh'),

]

common_urls = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('{}{}'.format(api_v1_pattern, 'docs'), swagger_view),
]

urlpatterns = api_urls + common_urls
