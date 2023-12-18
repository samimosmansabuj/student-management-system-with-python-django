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



def forget_password(request):
    
    return render(request, 'account/forget_password.html')