from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User

# As guided by the documentation when using a custom User model
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#a-full-example
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "first_name", "last_name", "date_of_birth", "is_staff", "is_active"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "date_of_birth"]}),
        ("Permissions", {
            "fields": [
                "is_admin", 
                "is_staff", 
                "is_active", 
                "is_superuser", 
                "groups", 
                "user_permissions"
                ]
            }),
        ("Important Dates", {"fields": ["last_login", "date_joined"]})
    ]

    add_fieldsets = [
        (None, {
            "classes": ["wide"],
            "fields": ["email", "first_name", "last_name", "date_of_birth", "password1", "password2"],
        })
    ]

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Register your models here.
admin.site.register(User, UserAdmin)
