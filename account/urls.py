from django.urls import path
from .views import Logout, Login, forget_password

urlpatterns = [
    path('logout/', Logout, name='logout'),
    path('login/', Login, name='login'),
    path('forget_password/', forget_password, name='forget_password'),
]