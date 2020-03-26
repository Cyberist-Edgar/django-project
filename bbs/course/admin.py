from django.contrib import admin
from .models import *


class AdminCourse(admin.ModelAdmin):
    list_display = ("name", "type", "major")
    list_per_page = 30
    ordering = ("name",)
    search_fields = ("name",)


class AdminCourseDes(admin.ModelAdmin):
    list_display = ("user_id", "teacher_id", "des")
    list_per_page = 30
    ordering = ("user_id",)
    search_fields = ("des",)


class AdminTeacher(admin.ModelAdmin):
    list_display = ("name", "course_id")
    list_per_page = 30
    ordering = ("name", )
    search_fields = ("name",)


class AdminMajor(admin.ModelAdmin):
    list_display = ("name", "academy")
    list_per_page = 30
    ordering = ("name", "academy")
    search_fields = ("name", )


admin.site.register(Course, AdminCourse)
admin.site.register(CourseDes, AdminCourseDes)
admin.site.register(Major, AdminMajor)
admin.site.register(TeacherOfCourse, AdminTeacher)
