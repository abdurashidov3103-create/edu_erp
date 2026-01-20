from django.db import models

from apps.core.models import BaseModel
from apps.students.models import Student

class Invoice(models.Model, BaseModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Invoice #{self.id} - {self.student}"


class Payment(models.Model , BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.invoice}"

