from django.urls import path
from staff.views import *

urlpatterns = [
    path('', staff_list, name='staff_list'),
    path('add-staff/', add_staff, name='add_staff'),
]