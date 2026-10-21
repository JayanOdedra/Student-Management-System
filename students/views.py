from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Student, Course
from .forms import StudentForm, CourseForm


# ─── Dashboard ────────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    active_students = Student.objects.filter(status='Active').count()
    latest_students = Student.objects.select_related('course').order_by('-created_at')[:5]
    return render(request, 'students/dashboard.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'active_students': active_students,
        'latest_students': latest_students,
    })


# ─── Student CRUD ─────────────────────────────────────────────────────────────

@login_required
def student_list(request):
    qs = Student.objects.select_related('course').all()

    q = request.GET.get('q', '').strip()
    course_filter = request.GET.get('course', '')
    dept_filter = request.GET.get('department', '')
    sem_filter = request.GET.get('semester', '')
    status_filter = request.GET.get('status', '')

    if q:
        qs = qs.filter(
            Q(full_name__icontains=q) |
            Q(email__icontains=q) |
            Q(student_id__icontains=q)
        )
    if course_filter:
        qs = qs.filter(course_id=course_filter)
    if dept_filter:
        qs = qs.filter(department__icontains=dept_filter)
    if sem_filter:
        qs = qs.filter(semester=sem_filter)
    if status_filter:
        qs = qs.filter(status=status_filter)

    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    courses = Course.objects.all()
    semesters = [str(i) for i in range(1, 9)]

    return render(request, 'students/student_list.html', {
        'page_obj': page_obj,
        'q': q,
        'courses': courses,
        'semesters': semesters,
        'course_filter': course_filter,
        'dept_filter': dept_filter,
        'sem_filter': sem_filter,
        'status_filter': status_filter,
        'total': qs.count(),
    })


@login_required
def student_add(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student added successfully!")
            return redirect('student_list')
        messages.error(request, "❌ Please fix the errors below.")
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student'})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student updated successfully!")
            return redirect('student_list')
        messages.error(request, "❌ Please fix the errors below.")
    return render(request, 'students/student_form.html', {
        'form': form, 'student': student, 'title': 'Edit Student'
    })


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student.objects.select_related('course'), pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "✅ Student deleted successfully!")
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})


# ─── Course CRUD ──────────────────────────────────────────────────────────────

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'students/course_list.html', {'courses': courses})


@login_required
def course_add(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Course added successfully!")
            return redirect('course_list')
        messages.error(request, "❌ Please fix the errors below.")
    return render(request, 'students/course_form.html', {'form': form, 'title': 'Add Course'})


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Course updated successfully!")
            return redirect('course_list')
        messages.error(request, "❌ Please fix the errors below.")
    return render(request, 'students/course_form.html', {'form': form, 'course': course, 'title': 'Edit Course'})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        if course.students.exists():
            messages.error(request, "❌ Cannot delete: students are enrolled in this course.")
            return redirect('course_list')
        course.delete()
        messages.success(request, "✅ Course deleted successfully!")
        return redirect('course_list')
    return render(request, 'students/course_confirm_delete.html', {'course': course})
