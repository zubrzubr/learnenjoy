from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from book.models import Book
from book.serializers import BookBaseSerializer, BookDetailSerializer
from common.permissions import BaseIsOwnerOrReadOnly


class BooksViewSet(viewsets.ModelViewSet):
    """
    Model view for books, presents:
        detail view, and list view for books.
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (BaseIsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookBaseSerializer
