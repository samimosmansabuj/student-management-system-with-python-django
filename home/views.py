from django.contrib.auth.decorators import login_required
from account.models import teacher, student, User
from department.models import Department
from django.http import HttpResponse
from django.shortcuts import render
from student.models import Invoice

@login_required(login_url='login')
def home(request):
    user = request.user
    
    if user.is_teacher == True:
        Teacher = teacher.objects.get(username=user)
        depart = Department.objects.get(title=Teacher.department)
        
        students = student.objects.all()
        depart_students = student.objects.filter(department=depart)
        depart_teacher = teacher.objects.filter(department=depart)
        
        context = {
            'Teacher': Teacher,
            'depart_students': depart_students,
            'depart_teacher': depart_teacher,
            'students': students
            }
        return render(request, 'home/teacher_home.html', context)
    
    elif user.is_student == True:
        Student = student.objects.get(username=user)
        context = {'Student': Student}
        return render(request, 'home/student_home.html', context)
    
    elif user.is_staff == True:
        Student = student.objects.all()
        department = Department.objects.all()
        Teacher = teacher.objects.all()
        
        invoice = Invoice.objects.all()
        total_revenue = 0
        for invoice in invoice:
            invoice_amount = invoice.amount
            total_revenue+=invoice_amount
        
        context = {'Student': Student, 'department': department, 'total_revenue': total_revenue, 'Teacher': Teacher}
        return render(request, 'home/home.html', context)

    # return render(request, 'home/home.html')
