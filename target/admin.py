from django.contrib import admin
from target.models import Target


class TargetAdmin(admin.ModelAdmin):
    """
    Target admins class
    """
    pass


admin.site.register(Target, TargetAdmin)
