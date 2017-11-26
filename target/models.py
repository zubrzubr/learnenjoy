from django.db import models
from django.utils.translation import ugettext as _


class Target(models.Model):
    """
    Target's model for tracking user's targets
    """
    name = models.CharField(_("Target's name"), max_length=255)
    description = models.TextField(_("Target's description"), max_length=1024)
    start_date = models.DateField(_("Target's start date"))
    end_date = models.DateField(_("Target's end date"))

    def __str__(self):
        return self.name
