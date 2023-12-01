# core/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Teacher, Student, Assignment, Class
from .forms import ClassForm, StudentForm, TeacherProfileForm, CustomUserCreationForm

# Public Views
def index(request):
    return render(request, 'core/index.html')

def teachers(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'core/teachers.html', {'teacher_list': teacher_list})

def students(request):
    student_list = Student.objects.all()
    return render(request, 'core/students.html', {'student_list': student_list})

def assignments(request):
    assignment_list = Assignment.objects.all()
    return render(request, 'core/assignments.html', {'assignment_list': assignment_list})

# Class Views
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'core/class_list.html', {'classes': classes, 'active_tab': 'classes'})

def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()

    return render(request, 'core/class_form.html', {'form': form})

def update_class(request, pk):
    my_class = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=my_class)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=my_class)

    return render(request, 'core/class_form.html', {'form': form})

def delete_class(request, pk):
    my_class = get_object_or_404(Class, pk=pk)
    my_class.delete()
    return redirect('class_list')

def class_detail(request, pk):
    my_class = get_object_or_404(Class, pk=pk)
    students = my_class.students.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.student_class = my_class
            student.save()
            return redirect('class_detail', pk=pk)
    else:
        form = StudentForm()

    return render(request, 'core/class_detail.html', {'class': my_class, 'students': students, 'form': form})

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'core/student_form.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'core/student_form.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

# Teacher Views
@login_required(login_url='account_login')
def teacher_profile(request):
    teacher = request.user.teacher

    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
    else:
        form = TeacherProfileForm(instance=teacher)

    return render(request, 'core/teacher_profile.html', {'form': form})

@login_required(login_url='account_login')
def some_view(request):
    teacher = request.user.teacher

    if not teacher.can_view_student_info():
        return HttpResponseForbidden("You don't have permission to view student information.")

    # Your view logic for displaying student information goes here
    students_in_teacher_class = Student.objects.filter(student_class=teacher.teacher_class)

    return render(request, 'core/some_view.html', {'students': students_in_teacher_class})

# Authentication Views
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful!')
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Admin Dashboard View
@login_required(login_url='account_login')
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@user_passes_test(lambda user: user.user_type == 'teacher' and user.has_perm('core.manage_teacher_profile'))
def manage_teacher_profile(request):
    # Assuming you have a Teacher model related to the CustomUser model
    teacher = request.user.teacher  # Get the teacher instance associated with the user

    if request.method == 'POST':
        # Assuming you have a TeacherProfileForm for updating teacher profiles
        form = TeacherProfileForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher profile updated successfully!')
        else:
            messages.error(request, 'Error updating teacher profile. Please check the form.')
    else:
        # Assuming you have a TeacherProfileForm for displaying/editing teacher profiles
        form = TeacherProfileForm(instance=teacher)

    return render(request, 'manage_teacher_profile.html', {'form': form})
