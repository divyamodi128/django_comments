from django.test import TestCase
from posts.models import Post
from src.tests import BasicSuperUserTest, BasicUserTest
from django.contrib.auth.models import User

# Create your tests here.
class TestPostSuperUser(BasicUserTest):
    
    def setUp(self):
        super(TestPostSuperUser, self).setUp()
        Post.objects.create(
            title='Testing Posts',
            content='First Content...',
            media_url='',
        )
    
    def test_updating_post(self):
        user = User.objects.get(username="Common")
        post = Post.objects.get(title='Testing Posts')
        post.title = 'Testing the post apis'
        self.assertEqual(post.title, 'Testing the post apis')
        post.content = 'Testing unit test'
        self.assertEqual(post.content, 'Testing unit test')
        