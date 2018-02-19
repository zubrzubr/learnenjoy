from rest_framework import serializers

from book.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for authors. Need for books serializers to present m to m relation and for
    author's api point.
    """
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'bio')


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for genres. Need for books serializers to present m to m relation and for
    author's api point.
    """
    class Meta:
        model = Genre
        fields = ('title', 'description')


class BookBaseSerializer(serializers.ModelSerializer):
    """
    Base serializer for books. Presents id, title and authors.
    """
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors')


class BookDetailSerializer(BookBaseSerializer):
    """
    Serializer for details view for books. Presents data with related fields (authors and genres).
    """
    genre = GenreSerializer(read_only=True, many=False)

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'authors', 'genre')
