from django.conf.urls import url, include
from rest_framework import routers

from book.views import BooksViewSet


router = routers.DefaultRouter()
router.register(r'books', BooksViewSet, base_name='books_view')


urlpatterns = [
    url(r'', include(router.urls)),
]
