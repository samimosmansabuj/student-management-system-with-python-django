from django.contrib import admin
from .models import User, student, teacher, Staff


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'id']
    
class studentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number', 'roll_no', 'gender']

class teachertAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number', 'id', 'gender']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'id', 'gender']


admin.site.register(User, UserAdmin)
admin.site.register(student, studentAdmin)
admin.site.register(teacher, teachertAdmin)
admin.site.register(Staff, StaffAdmin)

