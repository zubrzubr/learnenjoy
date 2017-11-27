from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser

from book.models import Book
from target.models import Target


class CustomUser(AbstractUser):
    """
    Custom user model to add new attributes to django user model.
    """
    bio = models.TextField(_("User's biography"), max_length=500, blank=True)
    country = models.CharField(_("User's country"), max_length=30, blank=True)
    city = models.CharField(_("User's city"), max_length=30, blank=True)
    birth_date = models.DateField(_("User's birth date"), null=True, blank=True)
    favorite_books = models.ManyToManyField(Book, related_name="users_favorite_books", null=True, blank=True)
    target = models.ManyToManyField(Target, related_name="users_targets")
