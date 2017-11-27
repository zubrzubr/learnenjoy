from django.contrib import admin
from custom_user.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """
    Custom user admins class
    """
    pass


admin.site.register(CustomUser, CustomUserAdmin)
