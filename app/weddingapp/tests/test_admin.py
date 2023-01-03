"""
Tests for the Django admin modifications.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='adminuser', password='password')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username='guestuser', password='password')

    def test_users_list(self):
        """Test that users are listed on the admin page."""
        url = reverse('admin:weddingapp_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
