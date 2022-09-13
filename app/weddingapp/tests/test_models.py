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
            user = get_user_model().objects.create_user(f'user{email}', "password", email=email)
            self.assertEqual(user.email, expected)
#It doesn't lowercase the first part because the capitalization of the first part of the email address is unique. Most of the email providers do not allow two email addresses with the same text, but different capitalization. But we don't know which system the user is using.