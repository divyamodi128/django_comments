from django.contrib import admin
from .models import AllUser

# Register your models here.
class AllUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_address', 'first_name', 'last_name']
    list_display_links = ['email_address']
    list_editable = ['username']
    search_fields = ['username', 'email_address']

admin.site.register(AllUser, AllUserAdmin)