from django.conf.urls import url, include
from django.contrib import admin


api_urls = [
    url(r'^api/v1/', include('book.urls')),
    url(r'^api/v1/', include('target.urls')),
    url(r'^api/v1/', include('custom_user.urls')),
]

common_urls = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns = api_urls + common_urls
