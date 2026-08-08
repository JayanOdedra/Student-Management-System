"""
urls.py - URL patterns for the students app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                                 # Dashboard
    path('add/', views.add_student, name='add_student'),               # Add Student
    path('students/', views.view_students, name='view_students'),      # View All
    path('update/<int:pk>/', views.update_student, name='update_student'),  # Update
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),  # Delete
]
