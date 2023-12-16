from django.urls import path
from .views import department_list, add_department, update_department

urlpatterns = [
    path('department-list/', department_list, name='department_list'),
    path('add-department/', add_department, name='add_department'),
    path('update-department/<int:id>/', update_department, name='update_department')
]