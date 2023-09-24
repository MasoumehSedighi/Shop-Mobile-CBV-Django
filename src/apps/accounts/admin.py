from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = [
        (None, {"fields": ("email", "password")}),        
        ("Permissions", {"fields": ["is_staff", "is_superuser"]})]
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_superuser", "groups")
    search_fields = ("email",)
    ordering = ("-id",)

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]



admin.site.register(User, UserAdmin)
