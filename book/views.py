from rest_framework import viewsets, serializers

from book.models import Book
from book.serializers import BookBaseSerializer, BookDetailSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """
    Model view for books, presents:
        detail view, and list view for books.
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookBaseSerializer
