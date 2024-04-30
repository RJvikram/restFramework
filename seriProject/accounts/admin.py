from django.contrib import admin
from accounts.models import Student
# Register your models here.

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('name','role','city')
