from django.contrib import admin
from reward.models import Reward


class RewardAdmin(admin.ModelAdmin):
    """
    Reward admins class
    """
    pass


admin.site.register(Reward, RewardAdmin)
