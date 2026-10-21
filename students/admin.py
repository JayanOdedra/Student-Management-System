from django.contrib import admin
from .models import Student, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'duration']
    search_fields = ['name', 'code', 'department']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'full_name', 'email', 'course', 'semester', 'status']
    list_filter = ['status', 'course', 'semester']
    search_fields = ['student_id', 'full_name', 'email']
    readonly_fields = ['student_id', 'created_at']
