"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test models"""

    def test_create_user_with_username_successful(self):
        """Test creating a user with the username is successful"""
        username = 'testuser'
        password = 'password'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
