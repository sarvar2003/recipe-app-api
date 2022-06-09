from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Custom user model tests"""

    def test_create_user_with_email(self):
        """Test that user is created successful with email"""
        email = 'test@email.com'
        password = 'secret1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user's email is normalized"""
        email = 'email@TEST.GMAIL'
        user = get_user_model().objects.create_user(email, 'secret1324')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'secret1234')
    
    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.comm',
            'secret122'
        ) 

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    