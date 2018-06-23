from django.db import models
from django.utils.translation import ugettext as _

from book.models import Book
from reward.models import Reward
from common.abstract_models import OwnerModel


class Target(OwnerModel):
    """
    Target's model for tracking user's targets
    """
    title = models.CharField(_("Target's name"), max_length=255)
    description = models.TextField(_("Target's description"), max_length=1024)
    book = models.ForeignKey(Book, related_name='targets', on_delete=models.PROTECT)
    reward = models.ForeignKey(Reward, related_name='targets', on_delete=models.PROTECT)
    start_date = models.DateField(_("Target's start date"))
    end_date = models.DateField(_("Target's end date"))
    current_page_progress = models.PositiveIntegerField(_("Current page progress"), default=0)

    def __str__(self):
        return self.title
