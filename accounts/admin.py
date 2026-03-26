from django.contrib import admin
from .models import CustomUser


class USERAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'mobile') 

admin.site.register(CustomUser, USERAdmin)