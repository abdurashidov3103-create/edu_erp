from django.db import models
from apps.accounts.models import User
from apps.core.models import BaseModel


class Teacher(models.Model, BaseModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.user.username


class TeacherProfile(models.Model, BaseModel):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    bio = models.TextField()
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.teacher.user.username
