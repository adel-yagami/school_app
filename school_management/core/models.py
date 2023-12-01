# core/models.py

from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)
    grade_level = models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    teacher_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def can_view_student_info(self):
        return self.user.has_perm('core.view_student_info')
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    student_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    def __str__(self):
        return self.username

# Function to create permissions
def create_permissions(sender, **kwargs):
    if kwargs['created']:
        content_type = ContentType.objects.get_for_model(CustomUser)

        # Create the 'view_student_info' permission
        Permission.objects.get_or_create(
            codename='view_student_info',
            name='Can view student information',
            content_type=content_type,
        )

        # Create the 'manage_teacher_profile' permission
        Permission.objects.get_or_create(
            codename='manage_teacher_profile',
            name='Can manage teacher profile',
            content_type=content_type,
        )

# Connect the function to the post-save signal of CustomUser
models.signals.post_save.connect(create_permissions, sender=CustomUser)
