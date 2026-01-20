from django.db import models
from apps.accounts.models import User
from apps.core.models import BaseModel


class Student(models.Model, BaseModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('graduated', 'Graduated'),
        ('dropped', 'Dropped'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.user.username


class StudentProfile(models.Model, BaseModel):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.student.user.username
