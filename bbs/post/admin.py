from django.contrib import admin
from .models import *


class AdminPost(admin.ModelAdmin):
    list_display = ("topic", "counter", "content")
    list_per_page = 30
    ordering = ("-date", "topic")
    search_fields = ("topic",)


admin.site.register(Post, AdminPost)
