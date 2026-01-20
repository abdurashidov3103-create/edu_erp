from django.db import models

from apps.core.models import BaseModel
from apps.groups.models import Group
from apps.teachers.models import Teacher

class Lesson(models.Model, BaseModel):
    VIDEO_TYPE = (
        ('upload', 'Upload'),
        ('youtube', 'YouTube'),
    )

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_type = models.CharField(max_length=20, choices=VIDEO_TYPE)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

