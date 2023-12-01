# core/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_dashboard, class_list, create_class, update_class, delete_class, index, teachers, students, assignments, student_list, create_student, update_student, delete_student, register

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('', index, name='index'),
    path('teachers/', teachers, name='teachers'),
    path('students/', students, name='students'),
    path('assignments/', assignments, name='assignments'),
    
    # Class-related URLs
    path('classes/', class_list, name='class_list'),
    path('classes/create/', create_class, name='create_class'),
    path('classes/update/<int:pk>/', update_class, name='update_class'),
    path('classes/delete/<int:pk>/', delete_class, name='delete_class'),

    # Student-related URLs
    path('students/', student_list, name='student_list'),
    path('students/create/', create_student, name='create_student'),
    path('students/update/<int:pk>/', update_student, name='update_student'),
    path('students/delete/<int:pk>/', delete_student, name='delete_student'),

    # Authentication URLs
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    # Add the create_student URL pattern
    path('create_student/', create_student, name='create_student'),
    # Add other URL patterns as needed
]
