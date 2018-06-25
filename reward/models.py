from django.db import models
from django.utils.translation import ugettext as _

from common.abstract_models import OwnerModel


class Reward(OwnerModel):
    """
    Rewards's model to present rewards which related to targets
    """
    name = models.CharField(_("Reward's name"), max_length=255)
    url = models.URLField(_("Link to reward"), null=True, blank=True)

    def __str__(self):
        return self.name
