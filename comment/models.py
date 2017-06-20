from django.db import models
from django.conf import settings
# from allusers.models import AllUser
from django.contrib.auth.models import User

# Create your models here.
def get_sentinel_user():
    return User.objects.get_or_create(username='Unknown')

class Comment(models.Model):
    custom_model = models.ForeignKey(
        settings.COMMENTS_BASED_MODEL,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    content   = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
