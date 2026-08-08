"""
models.py - Student database model using Django ORM.
"""

from django.db import models


class Student(models.Model):
    """Student model with basic fields for college management."""

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name} ({self.course})"
