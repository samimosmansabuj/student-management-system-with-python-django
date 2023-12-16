from django.urls import path
from .views import *

urlpatterns = [
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('teacher-list/', teacher_list, name='teacher'),
]