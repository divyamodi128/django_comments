from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' ,'custom_model', 'user']
    list_display_links = ['id']
    list_filter = ['timestamp', 'updated']
 
admin.site.register(Comment, CommentAdmin)