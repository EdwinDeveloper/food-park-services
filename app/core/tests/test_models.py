from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating a new user with an email successful"""
        email = "edwindeveloper@outlook.com"
        password = "test1234455"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))
