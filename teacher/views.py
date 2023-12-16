from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from department.models import Department
from account.models import teacher



# Create your views here.
@login_required(login_url='login')
def add_teacher(request):
    depart = Department.objects.all()
    context = {'department': depart}
    
    if request.method == 'POST':
        departmnt = request.POST['department']
        department = Department.objects.get(title=departmnt)
        
        teacher_designation = request.POST['teacher_designation']
        
        teacher_image = request.FILES.get('teacher_image')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        # date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number']
        # join_date = request.POST['join_date']
        job_experience = request.POST['job_experience']
        address = request.POST['address']
        username = request.POST['username']
        email = request.POST['email']
        
        # password = request.POST['password']
        # re_password = request.POST['re_password']
        
        user = teacher.objects.create(
            first_name=first_name, last_name=last_name, gender=gender, phone_number=phone_number, job_experience=job_experience, address=address, username=username, email=email, teacher_designation=teacher_designation,department=department, teacher_image=teacher_image
        )
        user.set_password(username)
        user.is_teacher = True
        user.save()
        
        if teacher_designation == 'Deaprtment Head':
            department.HOD = user.first_name+ ' '+user.last_name
            department.save()
        return redirect('teacher')
        
    return render(request, 'teacher/add_teacher.html', context)


@login_required(login_url='login')
def teacher_list(request):
    context = {}
    user = request.user
    if user.is_teacher:
        Teacher = teacher.objects.get(username=user)
        context['Teacher'] = Teacher
        depart = Department.objects.get(title=Teacher.department)
        Teach = teacher.objects.filter(department=depart)
        print(Teach)
    else:
        Teach = teacher.objects.all()
    
    item_per_page = 5
    paginator = Paginator(Teach, item_per_page)
    page = request.GET.get('page')
    try:
        teachers = paginator.page(page)
    except EmptyPage:
        teachers = paginator.page(1)
    except PageNotAnInteger:
        teachers = paginator.page(1)
    except InvalidPage:
        teachers = paginator.page(1)
    
    context['paginator'] = paginator
    context['teachers'] = teachers
    return render(request, 'teacher/teacher_list.html', context)

