from django.contrib import admin

# Register your models here.
from .models import UserProfile, UserProfileManager

admin.site.register(UserProfile)

