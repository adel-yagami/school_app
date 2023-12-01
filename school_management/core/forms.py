# core/forms.py

from django import forms
from .models import Class, Student, Teacher, CustomUser
from django.contrib.auth.forms import UserCreationForm

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'grade_level']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class']

class TeacherProfileForm(forms.ModelForm):
    # Assuming you have a ForeignKey field in the Teacher model for the class
    teacher_class = forms.ModelChoiceField(queryset=Class.objects.all(), empty_label=None)

    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'teacher_class']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
