from django.test import TestCase
from django.contrib.auth.models import User

class BasicUserTest(TestCase):
    def setUp(self):
        User.objects.create(
            username='Common',
            email='divtestpy@gmail.com',
            password='divyamodi'
        )
        User.objects.create_superuser(
            username='Super',
            email='modidivya16@gmail.com',
            password='divyamodi'
        )
    
    def test_super_user(self):
        common_user = User.objects.get(username='Common')
        super_user = User.objects.get(username='Super')
        import pdb; pdb.set_trace()
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(common_user.is_authenticated)