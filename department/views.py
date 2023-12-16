from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.models import student, teacher
from .models import Department


# Create your views here.
@login_required(login_url='login')
def department_list(request):
    depart = Department.objects.all()
    
    item_per_page = 5
    paginator = Paginator(depart, item_per_page)
    page = request.GET.get('page')
    
    try:
        depart = paginator.page(page)
    except EmptyPage:
        depart = paginator.page(1)
    except PageNotAnInteger:
        depart = paginator.page(1)
    except InvalidPage:
        depart = paginator.page(1)
    
    context = {'depart': depart, 'paginator': paginator, 'item_per_page': item_per_page}
    
    return render(request, 'department/department_list.html', context)

@login_required(login_url='login')
def add_department(request):
    if request.method == 'POST':
        department_code = request.POST['department_code']
        title = request.POST['title']
        established_date = request.POST['established_date']
        depart = Department.objects.create(department_code=department_code, title=title, established_date=established_date)
        depart.save()
        return redirect('department_list')
    
    return render(request, 'department/add_department.html')


@login_required(login_url='login')
def update_department(request, id):
    depart = Department.objects.get(id=id)
    Student = student.objects.filter(department=depart)
    Teachers = teacher.objects.all()
    context = {'depart': depart, 'Student': Student, 'Teachers': Teachers}
    
    if request.method == 'POST':
        department_code = request.POST['department_code']
        title = request.POST['title']
        HOD = request.POST['HOD']
        
        depart.title = title
        depart.department_code = department_code
        depart.HOD = HOD
        depart.save()
        return redirect('department_list')
        
    return render(request, 'department/edit_department.html', context)