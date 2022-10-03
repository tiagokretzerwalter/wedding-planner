"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from weddingapp import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ["id"]
    list_display = ["username"]
    list_filter = ["is_staff", "is_superuser"]


admin.site.register(models.User, UserAdmin)
