from rest_framework import viewsets

from book.models import Book
from book.serializers import BookDetailSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """
    Model view for books, presents:
        detail view, and list view for books.
    Response example:
    [
        {
            "id": 1,
            "title": "Book's title",
            "description": "Book's description",
            "authors": [
                {
                    "first_name": "Name",
                    "last_name": "Surname",
                    "bio": "Author's bio"
                }
            ],
            "genre": {
                "title": "Genre name",
                "description": "Genre description"
            },
        },
    ]
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
