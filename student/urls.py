from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/', add_student, name='add_student'),
    
    path('student-list/', all_student, name='students'),
    path('filter-student/', filter_student, name='filter_student'),
    
    path('student-details/<int:id>/', student_details, name='student_details'),
    
    
    path('payment-fail/', payment_fail, name='payment_fail'),
    path('payment-success/', payment_success, name='payment_success'),
    path('online-payment-processing/<int:id>/', online_payment_processing, name='online_payment_processing'),
    
    path('fees-collect/', fees_collect, name='fees_collect'),
    path('payment-confirm/<int:id>/', payment_confirm, name='payment_confirm'),
    
    path('registration-fee-confirm/<int:id>/', registration_fee_confirm, name='registration_fee_confirm'),
    path('registration-fee-confirm-processing/', registration_fee_confirm_processing, name='registration_fee_confirm_processing'),
    
    path('invoice/<int:id>/', invoice, name='invoice'),
    
    path('invoice-list/', invoice_list, name='invoice_list'),
    
    path('student-promotion/', student_promotion, name='student_promotion')
]