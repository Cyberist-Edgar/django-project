from django.contrib import admin
from .models import *


class AdminUser(admin.ModelAdmin):
    list_display = ("user", "sex", "academy", "grade")
    ordering = ("user",)
    list_per_page = 30
    search_fields = ("user", "academy")


admin.site.register(User, AdminUser)


