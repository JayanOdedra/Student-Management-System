"""
admin.py - Register Student model in Django admin panel.
"""

from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'course', 'mobile')
    search_fields = ('name', 'course')
    list_filter = ('course',)
