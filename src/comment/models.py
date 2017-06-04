from django.db import models
from django.conf import settings

# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Comment(models.Model):
    user = models.ForeignKey(
        settings.CUSTOMIZE_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    content   = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=False)
    updated   = models.DateTimeField(auto_now=False)
