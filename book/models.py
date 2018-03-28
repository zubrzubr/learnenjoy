from django.db import models
from django.utils.translation import ugettext as _


class Author(models.Model):
    """
    Model to define author for books
    """
    first_name = models.CharField(_("Author's first name"), max_length=255)
    last_name = models.CharField(_("Author's last name"), max_length=255)
    bio = models.TextField(_("Author's biography"), max_length=1024)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class Genre(models.Model):
    """
    Model to define genre for books
    """
    title = models.CharField(_("Genre title"), max_length=255)
    description = models.TextField(_("Genre description"), max_length=1024)

    def __str__(self):
        return self.title


class Book(models.Model):
    """
    Model to define book for user's targets
    """
    title = models.CharField(_("Book's name"), max_length=255)
    description = models.TextField(_("Book's description"), max_length=1024)
    authors = models.ManyToManyField(Author, related_name="authors_books")
    genres = models.ManyToManyField(Genre, related_name="books")
    page_count = models.PositiveIntegerField(_("Count of pages"), default=0)

    def __str__(self):
        return self.title
