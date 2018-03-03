from django.conf.urls import url, include
from django.contrib import admin


api_v1_pattern = r'^api/v1/'

api_urls = [
    url(api_v1_pattern, include('book.urls')),
    url(api_v1_pattern, include('target.urls')),
    url(api_v1_pattern, include('custom_user.urls')),
]

common_urls = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns = api_urls + common_urls
