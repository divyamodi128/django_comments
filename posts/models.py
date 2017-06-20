from django.db import models
from django.conf import settings
# from allusers.models import AllUser

# Create your models here.
# def get_default_user():
#     return AllUser.objects.get(id=3)
DEFAULT_USER_ID = 1

class Post(models.Model):
    """
    class: posts.models.Post
    """
    title = models.CharField(max_length=250, default='Post Coming Soon...')
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=None,
        default=DEFAULT_USER_ID,
    )
    media_url = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
