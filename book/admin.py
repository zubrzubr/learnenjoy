from django.contrib import admin
from book.models import Book, Genre, Author


class AuthorAdmin(admin.ModelAdmin):
    """
    Author admins class
    """
    pass


class GenreAdmin(admin.ModelAdmin):
    """
    Book admins class
    """
    pass


class BookAdmin(admin.ModelAdmin):
    """
    Book admins class
    """
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
