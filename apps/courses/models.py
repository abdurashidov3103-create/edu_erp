from django.db import models

from apps.core.models import BaseModel


class Course(models.Model, BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in months")

    def __str__(self):
        return self.name
