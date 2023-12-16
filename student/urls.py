from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/', add_student, name='add_student'),
    
    path('student-list/', all_student, name='students'),
    path('filter-student/', filter_student, name='filter_student'),
    
    path('student-details/<int:id>/', student_details, name='student_details'),
    
    path('fees-collect/', fees_collect, name='fees_collect'),
    path('payment-confirm/<int:id>/', payment_confirm, name='payment_confirm'),
    path('invoice/<int:id>/', invoice, name='invoice'),
    
    path('invoice-list/', invoice_list, name='invoice_list'),
    
    path('student-promotion/', student_promotion, name='student_promotion')
]