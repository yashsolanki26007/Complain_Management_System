from django.contrib import admin
from .models import Complaint, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'enrollment_no', 'department', 'category', 'status', 'submitted_at']
    list_filter = ['status', 'category', 'department']
    search_fields = ['student_name', 'enrollment_no']