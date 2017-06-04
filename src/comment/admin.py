from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp', 'updated']
    list_display_links = ['user']
    list_filter = ['timestamp', 'updated']
    search_fields =['user', 'content']
 
admin.site.register(Comment, CommentAdmin)