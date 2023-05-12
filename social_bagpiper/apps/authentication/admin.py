from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "profile_photo",)

admin.site.register(User, UserAdmin)