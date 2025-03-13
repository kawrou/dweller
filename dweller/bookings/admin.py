from django.contrib import admin
from .models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ["user", "destination"]
    fieldsets = [(None, {"fields": ["user", "destination"]})]

    search_fields = ["user"]
    ordering = ["user"]
    filter_horizontal = []


admin.site.register(Booking, BookingAdmin)