from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    father_name = models.CharField(max_length=150)

    student_class = models.CharField(max_length=20)

    section = models.CharField(max_length=10)

    parent_contact = models.CharField(max_length=20)

    profile_picture = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    result_pdf = models.FileField(
        upload_to="results/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
