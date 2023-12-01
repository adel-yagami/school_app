# core/admin.py

from django.contrib import admin
from .models import Teacher, Student, Assignment, Class


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Class)
