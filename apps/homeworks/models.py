from django.db import models

from apps.core.models import BaseModel
from apps.lessons.models import Lesson
from apps.teachers.models import Teacher

class Homework(models.Model, BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

