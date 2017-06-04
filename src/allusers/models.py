from django.db import models

# Create your models here.
class AllUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Personal Informations
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    # Permissions
    # Still to come
    # Important Dates
    created_date = models.DateTimeField(auto_now_add=True)
    last_login   = models.DateTimeField(auto_now=True)