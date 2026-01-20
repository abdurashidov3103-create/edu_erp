from django.db import models

from apps.core.models import BaseModel
from apps.courses.models import Course
from apps.teachers.models import Teacher
from apps.students.models import Student

class Group(models.Model, BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} ({self.start_date})"


class GroupMember(models.Model, BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'group')

    def __str__(self):
        return f"{self.student} → {self.group}"

