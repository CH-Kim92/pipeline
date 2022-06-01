from django.contrib import admin
from .models import userinfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(userinfo)