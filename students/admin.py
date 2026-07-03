from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "student_id",
        "first_name",
        "last_name",
        "student_class",
        "section",
    )

    search_fields = (
        "student_id",
        "first_name",
        "last_name",
    )