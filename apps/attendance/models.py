from django.db import models

from apps.core.models import BaseModel
from apps.lessons.models import Lesson
from apps.students.models import Student

class Attendance(models.Model, BaseModel):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('lesson', 'student')

    def __str__(self):
        return f"{self.student} - {self.lesson} ({self.status})"

