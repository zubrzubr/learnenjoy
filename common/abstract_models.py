from django.db import models


class OwnerModel(models.Model):
    """
    Add to models owner field. By default on delete policy is 'set_null'
    """
    user_on_delete_policy = 'set_null'

    on_delete_policy_mapping = {
        'cascade': models.CASCADE,
        'protect': models.PROTECT,
        'set': models.SET,
        'set_null': models.SET_NULL,
        'set_default': models.SET_DEFAULT,
        'do_nothing': models.DO_NOTHING,
    }

    owner = models.ForeignKey(
        'custom_user.CustomUser', null=True, on_delete=on_delete_policy_mapping.get(user_on_delete_policy)
    )

    class Meta:
        abstract = True
