from django.contrib import admin
from .models import Virus


# Register your models here.
class VirusAdmin(admin.ModelAdmin):
    list_display = ("name", "ename", "value", "susnum", "deathnum", "curenum", "city")
    search_fields = ("name",)


admin.site.register(Virus, VirusAdmin)
