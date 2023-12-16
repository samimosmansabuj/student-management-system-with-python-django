from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.models import Staff

# Create your views here.
@login_required(login_url='login')
def staff_list(request):
    staff = Staff.objects.all()
    context = {'staff': staff}
    return render(request, 'staff/staff_list.html', context)

@login_required(login_url='login')
def add_staff(request):
    
    if request.method == 'POST':
        staff_image = request.FILES.get('staff_image')
        first_name = request.POST['first_name']
        staff_designation = request.POST['staff_designation']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        job_experience = request.POST['job_experience']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        print(staff_designation)
        
        staff = Staff.objects.create(name=first_name, gender=gender, phone_number=phone_number, staff_designation=staff_designation, address=address, staff_image=staff_image, job_experience=job_experience, username=username, email=email)
        staff.is_staff = True
        staff.is_varified = True
        staff.set_password(username)
        
        if staff_designation == 'Chief Administrative Officer':
            print(staff_designation)
            staff.is_adminstaff = True
        elif staff_designation == 'Manager':
            staff.is_adminstaff = True
        staff.save()
        return redirect('staff_list')
        
    return render(request, 'staff/add_staff.html')