from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successful"""
        email = 'edwindeveloper@outlook.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        # self.assertTrue(1,2)

    def test_new_user_email_normalized(self):
        """Test for the email for a new user is normalized"""
        email = 'edwindeveloper@OUTLOOK.com'
        user = get_user_model().objects.create_user(email, 'Test123')
        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test reating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234')

    def test_create_the_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'edwindeveloper@outlook.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
