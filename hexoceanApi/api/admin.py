from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import AppUser, UserTier


class UserInline(admin.StackedInline):
    model = AppUser
    can_delete = False
    verbose_name_plural = "Users"

class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]

class TierAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserTier, TierAdmin)
