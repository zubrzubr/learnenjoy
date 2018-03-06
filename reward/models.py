from django.db import models
from django.utils.translation import ugettext as _


class Reward(models.Model):
    """
    Rewards's model to present rewards which related to targets
    """
    name = models.CharField(_("Reward's name"), max_length=255)
    url = models.URLField(_("Link to reward"))

    def __str__(self):
        return self.name
