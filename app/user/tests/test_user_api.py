"""
Tests for the user API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


class UserApiTests(TestCase):
    """Test the features of the user API."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password',
        )
        self.admin = get_user_model().objects.create_superuser(
            username='testadmin',
            password='password',
        )

    def test_create_user_success(self):
        """Test admin creating a user is successful."""
        payload = {
            'username': 'testusername',
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'Username',
        }

        self.client.force_login(self.admin)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(username=payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_without_login(self):
        """Test creating a user without authentication fails."""
        payload = {
            'username': 'testusername',
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'Username',
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_as_not_admin(self):
        """
        Test creating a user logged as common user (not admin) fails.
        """
        payload = {
            'username': 'testusername',
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'Username',
        }

        self.client.force_login(self.user)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_same_username(self):
        """
        Test creating a user logged as common user (not admin) fails.
        """
        payload = {
            'username': 'testuser',
            'password': 'password',
        }

        self.client.force_login(self.admin)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
