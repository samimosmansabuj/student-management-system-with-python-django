from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from account.models import teacher, student, User
from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.
@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

def Login(request): 
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            users = User.objects.get(username=username)
            print(users.is_student)
            if users.is_teacher == True:
                user = authenticate(username=username, password=password)
                if not user:
                    messages.warning(request, "wrong Password!")
                login(request, user)
                return redirect('home')
            elif users.is_student == True:
                print(username, password)
                user = authenticate(username=username, password=password)
                if not user:
                    messages.warning(request, "wrong Password!")
                login(request, user)
                return redirect('home')
            
            elif users.is_staff == True:
                user = authenticate(username=username, password=password)
                if not user:
                    messages.warning(request, "wrong Password!")
                login(request, user)
                return redirect('home')
        else:
            messages.warning(request, "Invalid Username!")
            return redirect('login')
    return render(request, 'account/login.html')

import random
from django.core.mail import send_mail
from django.conf import settings

def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = random.randint(111111, 999999)
        Student = student.objects.get(email=email)
        Student.otp_token = otp
        Student.save()
        
        subject = 'Verify OTP For Forget Password!'
        message = f'Dear user, Your OTP is {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
        
        return render(request, 'account/forget_password_reset.html', {'email': email})
    
    return render(request, 'account/forget_password.html')

def forget_password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('password')
        
        Student = student.objects.get(email=email)
        if Student.otp_token != otp:
            messages.warning(request, 'OTP does not match!')
            return redirect(request.META['HTTP_REFERER'])
        
        Student.set_password(new_password)
        Student.otp_token = None
        Student.save()
        messages.success(request, 'Password Change Successfully!')
        return redirect('login')
        
    return None


