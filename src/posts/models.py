from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, default='Post Coming Soon...')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    media_url = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title
