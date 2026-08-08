"""
forms.py - Student form with validation rules.
"""

from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    """Form for adding and updating student records with validation."""

    class Meta:
        model = Student
        fields = ['name', 'age', 'course', 'mobile']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student full name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age (16-35)'
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. BCA, MCA, B.Tech'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 10-digit mobile number',
                'maxlength': '10'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Student name cannot be empty.")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise forms.ValidationError("Age must be a numeric value.")
        if not (16 <= age <= 35):
            raise forms.ValidationError("Age must be between 16 and 35.")
        return age

    def clean_course(self):
        course = self.cleaned_data.get('course', '').strip()
        if not course:
            raise forms.ValidationError("Course cannot be empty.")
        return course

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Mobile number must contain exactly 10 digits.")
        return mobile
