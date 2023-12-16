from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'department_code', 'HOD', 'established_date']

admin.site.register(Department, DepartmentAdmin)