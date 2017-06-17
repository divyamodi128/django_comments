from django.db import models
from django.conf import settings
from allusers.models import AllUser

# Create your models here.
def get_sentinel_user():
    return AllUser.objects.get_or_create(username='Unknown')

class Comment(models.Model):
    post = models.ForeignKey(
        settings.COMMENTS_BASED_MODEL,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.COMMENTS_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    content   = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
