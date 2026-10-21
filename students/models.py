from django.db import models
from django.core.validators import RegexValidator


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, help_text="e.g. 3 Years, 2 Semesters")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"


GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]
SEMESTER_CHOICES = [(str(i), f'Semester {i}') for i in range(1, 9)]

mobile_validator = RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit mobile number.')


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, validators=[mobile_validator])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='students')
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    address = models.TextField(blank=True)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Auto-generate student_id like STU0001 on first save
        if not self.student_id:
            super().save(*args, **kwargs)
            self.student_id = f"STU{self.pk:04d}"
            Student.objects.filter(pk=self.pk).update(student_id=self.student_id)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id} - {self.full_name}"
