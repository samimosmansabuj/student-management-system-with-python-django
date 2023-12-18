from django.urls import path
from .views import Logout, Login, forget_password, forget_password_reset

urlpatterns = [
    path('logout/', Logout, name='logout'),
    path('login/', Login, name='login'),
    path('forget-password/', forget_password, name='forget_password'),
    path('forget-password-reset/', forget_password_reset, name='forget_password_reset'),
]