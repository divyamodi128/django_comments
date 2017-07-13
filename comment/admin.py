from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
<<<<<<< Updated upstream
    list_display = ['custom_model', 'user']
    # list_display_links = ['id']
<<<<<<< Updated upstream

=======
=======
    list_display = ['id' ,'custom_model', 'user']
    list_display_links = ['id']
>>>>>>> Stashed changes
>>>>>>> Stashed changes
    list_filter = ['timestamp', 'updated']
 
admin.site.register(Comment, CommentAdmin)