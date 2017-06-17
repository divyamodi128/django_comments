from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated', 'timestamp']
    list_display_links = ['id']
    list_editable = ['title']
    list_filter = ['timestamp', 'updated']

    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)