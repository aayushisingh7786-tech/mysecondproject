from django.contrib import admin
from .models import Student

# This makes the Student table visible in the Admin Panel
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'course', 'joined_date')
    search_fields = ('name', 'roll_no')
