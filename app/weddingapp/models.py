"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    username = models.CharField(
        "Username",
        unique=True,
        max_length=150,
        help_text="It is the combination of the guest's first and last name"
    )
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
