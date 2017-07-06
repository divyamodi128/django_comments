from django.db import models
from django.conf import settings
# from allusers.models import AllUser
from django.contrib.auth.models import User

# Create your models here.
def get_sentinel_user():
    return User.objects.get_or_create(username='Unknown')

# def get_parent_comment(pk):
#     return Comment.objects.get(id=pk)

class Comment(models.Model):
    custom_model = models.ForeignKey(
        settings.COMMENTS_BASED_MODEL,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    parent_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=False, null=True
    )
    content   = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)

    def children(self):
        return Comment.objects.filter(parent_comment=self)
    
    def __str__(self):
        return str(self.id)
    
    def get_user_name(self):
        return str(self.user.username)
