from django.db import models

from apps.core.models import BaseModel
from apps.homeworks.models import Homework
from apps.students.models import Student

class Submission(models.Model, BaseModel):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True)
    file_answer = models.FileField(upload_to='submissions/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(blank=True, null=True)
    teacher_comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('homework', 'student')

    def __str__(self):
        return f"{self.student} - {self.homework}"
