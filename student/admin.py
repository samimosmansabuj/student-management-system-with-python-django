from django.contrib import admin
from .models import *

# Register your models here.
class SemestersAdmin(admin.ModelAdmin):
    list_display = ['title', 'Student', 'start_date', 'is_complete', 'id']

class InstallmentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'discount', 'semester', 'created_date', 'id']




admin.site.register(Semesters, SemestersAdmin)
admin.site.register(Installments, InstallmentsAdmin)
admin.site.register(Invoice)
admin.site.register(Registration_fees)