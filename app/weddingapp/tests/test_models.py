"""
Tests for models
"""
from sqlite3 import IntegrityError
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test models"""

    def create_user_helper(self):
        """Helper method for creating a new user"""
        username = 'testuser'
        password = 'password'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        return user

    def test_create_user_with_username_successful(self):
        """Test creating a user with the username is successful"""
        user = self.create_user_helper()

        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password"))

    def test_username_is_case_insensitive(self):
        """Test username is case insensitive for new users"""
        user = self.create_user_helper()
        users = ['TestUser', 'TESTUSER', 'Testuser']

        for user in users:
            get_user_model().objects.create_user(
                username=user,
                password="password"
            )
            self.assertRaises(IntegrityError)

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
            [None, ""]
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                f'user{email}', "password", email=email)
            self.assertEqual(user.email, expected)

    def test_new_user_without_username_raises_error(self):
        """Test that creating a user without an username raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "password")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'username',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
