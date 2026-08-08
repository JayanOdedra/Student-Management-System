"""
views.py - All views for Student Management System (CRUD + Search).
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def home(request):
    """Dashboard view showing student statistics."""
    total_students = Student.objects.count()
    return render(request, 'students/home.html', {'total_students': total_students})


def add_student(request):
    """Add a new student record."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student Added Successfully!")
            return redirect('view_students')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


def view_students(request):
    """View all students with optional search by ID or name."""
    query = request.GET.get('q', '').strip()
    students = Student.objects.all()

    if query:
        # Search by student ID (if numeric) or name (case-insensitive)
        if query.isdigit():
            students = students.filter(Q(id=int(query)) | Q(name__icontains=query))
        else:
            students = students.filter(Q(name__icontains=query))

    return render(request, 'students/view_students.html', {
        'students': students,
        'query': query,
        'total': students.count(),
    })


def update_student(request, pk):
    """Edit and update an existing student record."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student Updated Successfully!")
            return redirect('view_students')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/update_student.html', {'form': form, 'student': student})


def delete_student(request, pk):
    """Delete a student record (POST only for safety)."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "✅ Student Deleted Successfully!")
        return redirect('view_students')

    return render(request, 'students/delete_confirm.html', {'student': student})
