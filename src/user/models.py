from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=5, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username