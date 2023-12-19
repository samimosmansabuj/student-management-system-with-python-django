from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager
from department.models import Department

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=40, validators=[UnicodeUsernameValidator], unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_adminstaff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    
    class Meta: 
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.username

class Staff(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    RELIGION = (
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Chirstian', 'Chirstian'),
        ('Buddist', 'Buddist'),
        ('Others', 'Others'),
    )
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=False)
    phone_number = models.TextField()
    join_date = models.DateTimeField(auto_now_add=True)
    staff_designation = models.CharField(max_length=300, blank=True, null=True)
    
    date_of_birth = models.DateField(blank=True, null=True)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=5, blank=True, null=False)
    address = models.TextField(blank=True, null=True)
    religion = models.CharField(choices=RELIGION, max_length=10, blank=True, null=False)
    staff_image = models.ImageField(upload_to='staff/img/', blank=True, null=False)
    job_experience = models.PositiveIntegerField(blank=True, null=False)
    
    
    is_varified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name


class student(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    RELIGION = (
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Chirstian', 'Chirstian'),
        ('Buddist', 'Buddist'),
        ('Others', 'Others'),
    )
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=False)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=5, blank=True, null=False)
    roll_no = models.PositiveIntegerField(blank=True)
    religion = models.CharField(choices=RELIGION, max_length=10, blank=True, null=False)
    phone_number = models.TextField()
    student_image = models.ImageField(upload_to='student/img/', blank=True, null=False, default='student_avatar.png/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_deparment', blank=True, null=True)
    semester = models.CharField(max_length=40)
    tuition_fees_discount = models.IntegerField(blank=True, null=True)
    
    otp_token = models.CharField(max_length=6, blank=True, null=True)
    
    is_varified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'



class teacher(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    RELIGION = (
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Chirstian', 'Chirstian'),
        ('Buddist', 'Buddist'),
        ('Others', 'Others'),
    )
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teacher_designation = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=5, blank=True, null=False)
    address = models.TextField(blank=True, null=True)
    religion = models.CharField(choices=RELIGION, max_length=10, blank=True, null=False)
    teacher_image = models.ImageField(upload_to='teacher/img/', blank=True, null=False)
    job_experience = models.PositiveIntegerField(blank=True, null=False)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    is_varified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.first_name
    
    
    