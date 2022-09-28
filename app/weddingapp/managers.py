"""User model manager"""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, username, password=None, email=None, **extra_fields):
        """
        Create, save and return a new user with given username and password
        """
        if not username:
            raise ValueError("Please provide an username.")
        user = self.model(username=username,
                          email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create and return a new superuser"""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, username):
        """Make username case insensitive"""
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)

        return self.get(**{case_insensitive_username_field: username})
