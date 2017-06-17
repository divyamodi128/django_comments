from django.test import TestCase
from django.contrib.auth.models import User

class BasicSuperUserTest(TestCase):
    """Testing with Super User"""
    def setUp(self):
        User.objects.create_superuser(
            username='Super',
            email='modidivya16@gmail.com',
            password='divyamodi'
        )

    def test_super_user(self):
        super_user = User.objects.get(username='Super')  
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_authenticated)
        
class BasicUserTest(TestCase):
    """Testing with Common User"""
    def setUp(self):
        User.objects.create(
            username='Common',
            email='divtestpy@gmail.com',
            password='divyamodi'
        )
        
    def test_user_authentications(self):
        common_user = User.objects.get(username='Common')
        self.assertTrue(common_user.is_active)
        self.assertFalse(common_user.is_staff)
        self.assertFalse(common_user.is_superuser)
        self.assertTrue(common_user.is_authenticated)