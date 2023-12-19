from student.models import Semesters, Installments, Invoice, Registration_fees
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.loader import get_template
from account.models import student, teacher, User
from department.models import Department
from notifications.signals import notify
from django.core.mail import send_mail
from sslcommerz_lib import SSLCOMMERZ
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from xhtml2pdf import pisa
from .models import *
import random




# ---------------------Add Student Section Start------------------
@login_required(login_url='login')
def add_student(request):
    user = request.user
    if user.is_student == True:
        return redirect('home')
    
    department = Department.objects.all()
    context = {'department': department}
    
    if user.is_teacher == True:
        Teacher = teacher.objects.get(username=user)
        context['Teacher'] = Teacher
    
    if request.method == 'POST':
        department = request.POST['department']
        depart = Department.objects.get(title=department)
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        roll_no = request.POST['roll_no']
        blood_group = request.POST['blood_group']
        religion = request.POST['religion']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        image = request.FILES.get('image')
        username = 'user'+phone_number
        print(username)
        password = roll_no
        semester = request.POST['semester']
        if request.POST['weiver_tuition_fees']:
            weiver_tuition_fees = request.POST['weiver_tuition_fees']
        else:
            weiver_tuition_fees = 0
        
        new_student = student.objects.create(username=username, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, gender=gender, roll_no=roll_no, blood_group=blood_group, religion=religion, email=email, department=depart, phone_number=phone_number, semester=semester, tuition_fees_discount=weiver_tuition_fees)
        if image:
            new_student.student_image=image
        new_student.set_password(password)
        new_student.is_student = True
        new_student.is_varified = True
        new_student.save()
        
        semester = Semesters.objects.create(Student=new_student, title=semester)
        semester.save()
        
        amount = 3750 - (3750 * int(weiver_tuition_fees)/100)
        first_installment = Installments.objects.create(semester=semester, title="1st Installment", discount=weiver_tuition_fees, amount=amount)
        first_installment.save()
        
        second_installment = Installments.objects.create(semester=semester, title="2nd Installment", discount=weiver_tuition_fees, amount=amount)
        second_installment.save()
        
        third_installment = Installments.objects.create(semester=semester, title="3rd Installment", discount=weiver_tuition_fees, amount=amount)
        third_installment.save()
        
        fourth_installment = Installments.objects.create(semester=semester, title="4th Installment", discount=weiver_tuition_fees, amount=amount)
        fourth_installment.save()
        
        registration_amount = 1600
        registration_fees = Registration_fees.objects.create(
            Student = new_student,
            semester = semester,
            amount = registration_amount,
        )
        registration_fees.save()
        
        send_notification_add_student(new_student)
        send_mail_student_add(email, username, password)
        
        return redirect('students')
        
    return render(request, 'student/add_student.html', context)



def send_notification_add_student(new_student):
    admin = User.objects.get(id=5)
    verb=f"Congratulations {new_student.first_name}, Welcome to Our New Student!"
    print('admin: ', admin, '   student: ',student, '   verb: ', verb)
    notify.send(admin, recipient=new_student, verb=verb)



def send_mail_student_add(email, username, password):
    subject = 'Congratulations For Admission Complete in NPI'
    
    message = f'''Dear Student
    Your Mail: {email}
    Your Username: {username}
    Your Password: {password}'''
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
# ---------------------Add Student Section Start------------------


@login_required(login_url='login')
def all_student(request):
    context = {}
    user = request.user
    if user.is_student == True:
        return redirect('home')
    
    if user.is_teacher:
        Teacher = teacher.objects.get(username=user)
        context['Teacher'] = Teacher
        depart = Department.objects.get(title=Teacher.department)
        students = student.objects.filter(department=depart).order_by('roll_no')
    else:
        students = student.objects.all().order_by('roll_no')
    
    department = Department.objects.all()
    context['department'] = department
    context['students'] = students

    return render(request, 'student/student_list.html', context)

@login_required(login_url='login')
def filter_student(request):
    user = request.user
    if user.is_student == True:
        return redirect('home')
    try:
        request.GET['reset']
        return redirect('students')
    except:

        context = {}
        depart = request.GET['department']
        semester = request.GET['semester']
        search_kay = request.GET['search_kay']
        context['depart'] = depart
        context['semester'] = semester
        context['search_kay'] = search_kay
        
        if depart and semester:
            departm = Department.objects.get(title=depart)
            students = student.objects.filter(department=departm, semester=semester).order_by('roll_no')
        elif depart:
            departm = Department.objects.get(title=depart)
            students = student.objects.filter(department=departm).order_by('roll_no')
        elif semester:
            students = student.objects.filter(semester=semester).order_by('roll_no')
        else:
            students = student.objects.all().order_by('roll_no')
            if not search_kay:
                user_not_fount = "Student Not Found!"
                context['user_not_fount'] = user_not_fount

        if search_kay:
                if students.filter(first_name__icontains=search_kay):
                    students = students.filter(first_name__icontains=search_kay).order_by('roll_no')
                else:
                    user_not_fount = "Student Not Found!"
                    context['user_not_fount'] = user_not_fount
                    students = student.objects.all().order_by('roll_no')
        
        department = Department.objects.all()
        context['department'] = department
        context['students'] = students
        return render(request, 'student/student_list.html', context)




@login_required(login_url='login')
def student_details(request, id):
    context = {}
    user = request.user
    if user.is_teacher:
        Teacher = teacher.objects.get(username=user)
        context['Teacher'] = Teacher
    elif user.is_student:
        Student = student.objects.get(username=user)
        context['Student'] = Student

    single_student = student.objects.get(id=id)
    semester = Semesters.objects.filter(Student=single_student)
    context['single_student'] = single_student
    context['semester'] = semester
    
    return render(request, 'student/student_details.html', context)



@login_required(login_url='login')
def student_promotion(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        res = request.POST['result']
        result = float(res)
        semester = request.POST['semester']
        Student = student.objects.get(roll_no=roll_no)
        Student_Semester = Student.Students.all()
        print(Student_Semester)
        weiver_tuition_fees = Student.tuition_fees_discount
        
        for Student_Semester in Student_Semester:
            if Student_Semester.title == semester:
                Student_Semester.result = result
                Student_Semester.is_complete = True
                Student_Semester.save()
                
                if semester == '1st Semester':
                    semester = Semesters.objects.create(Student=Student, title='2nd Semester')
                    semester.save()
                elif semester == '2nd Semester':
                    semester = Semesters.objects.create(Student=Student, title='3rd Semester')
                    semester.save()
                elif semester == '3rd Semester':
                    semester = Semesters.objects.create(Student=Student, title='4th Semester')
                    semester.save()
                elif semester == '4th Semester':
                    semester = Semesters.objects.create(Student=Student, title='5th Semester')
                    semester.save()
                elif semester == '5th Semester':
                    semester = Semesters.objects.create(Student=Student, title='6th Semester')
                    semester.save()
                elif semester == '6th Semester':
                    semester = Semesters.objects.create(Student=Student, title='7th Semester')
                    semester.save()
                elif semester == '7th Semester':
                    semester = Semesters.objects.create(Student=Student, title='8th Semester')
                    semester.save()
                elif semester == '8th Semester':
                    Student.semester = 'Complete'
                    Student.save()
                    messages.success(request, 'Congratulations! Graduation Complete.')
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    messages.warning(request, 'Wrong Input!')
                    return HttpResponse('Wrong Input')
                
                Student.semester = semester.title
                Student.save()
                
                amount = 3750 - (3750 * int(weiver_tuition_fees)/100)
                first_installment = Installments.objects.create(semester=semester, title="1st Installment", discount=weiver_tuition_fees, amount=amount)
                first_installment.save()
                
                second_installment = Installments.objects.create(semester=semester, title="2nd Installment", discount=weiver_tuition_fees, amount=amount)
                second_installment.save()
                
                third_installment = Installments.objects.create(semester=semester, title="3rd Installment", discount=weiver_tuition_fees, amount=amount)
                third_installment.save()
                
                
                fourth_installment = Installments.objects.create(semester=semester, title="4th Installment", discount=weiver_tuition_fees, amount=amount)
                fourth_installment.save()
                
                registration_amount = 1600 if semester.title=='2nd Semester' or semester.title=='3rd Semester' else 1800
                
                registration_fees = Registration_fees.objects.create(
                    Student = Student,
                    semester = semester,
                    amount = registration_amount,
                )
                registration_fees.save()
                
        return redirect(request.META['HTTP_REFERER'])




# ------------------------Fees Collection Section start----------------------------
@login_required(login_url='login')
def invoice_list(request):
    invoices = Invoice.objects.all().order_by('-id')
    context = {'invoices': invoices}
    return render(request, 'fees/invoice_list.html', context)


@login_required(login_url='login')
def fees_collect(request):
    context = {}
    user = request.user
    if user.is_teacher == True:
        Teacher = teacher.objects.get(username=user)
        context['Teacher'] = Teacher
        
    if request.method == 'POST':
        student_roll = request.POST['student_roll']
        user = request.user
        
        if user.is_teacher:
            Teacher = teacher.objects.get(username=user)
            context['Teacher'] = Teacher
            depart = Department.objects.get(title=Teacher.department)
        
            if not student.objects.filter(roll_no=student_roll, department=depart).exists():
                messages.warning(request, "Invalid Roll Number!")
                return redirect('fees_collect')
        else:
            if not student.objects.filter(roll_no=student_roll).exists():
                messages.warning(request, "Invalid Roll Number!")
                return redirect('fees_collect')

        students = student.objects.get(roll_no=student_roll)
        Sem = Semesters.objects.filter(Student=students)
        context['student'] = students
        context['semesters'] = Sem
        
        return render(request, 'fees/student_fees_details.html', context)
    
    return render(request, 'fees/fees_collect.html')



@login_required(login_url='login')
def registration_fee_confirm(request, id):
    try:
        registration = Registration_fees.objects.get(id=id)
        context = {'registration': registration}
        return render(request, 'fees/payment_confirm.html', context)
    except:
        return HttpResponse('Wrong Input')

@login_required(login_url='login')
def registration_fee_confirm_processing(request):
    if request.method == 'POST':
        registration_id = request.POST['registration_id']
        
        name = request.POST['name']
        payment_method = request.POST['payment_method']
        registration = Registration_fees.objects.get(id=registration_id)
        
        if payment_method == 'Cash':
            registration.is_paid = True
            registration.payment_method = payment_method
            registration.save()
            
            invoice = Invoice.objects.create(
                student = registration.Student,
                semester = registration.semester,
                registration_fees = registration,
                Invoice_id = random.randint(1111111111, 9999999999),
                amount = registration.amount
            )
            invoice.save()
            messages.success(request, "Paid Recived Successfully!")
            return redirect(request.META['HTTP_REFERER'])
        
        elif payment_method == 'Bkash':
            amount = registration.amount
            name = registration.Student.first_name+' '+registration.Student.last_name
            email = registration.Student.email
            phone_number = registration.Student.phone_number
            address = registration.Student.address
            product_name = registration.title
            product_category = registration.semester.title
            tran_id = registration.id
            data = {'amount': amount, 'name': name, 'email': email, 'phone_number': phone_number, 'address':address, 'product_name': product_name, 'product_category': product_category, 'tran_id': tran_id}
            return online_payment(data)




@login_required(login_url='login')
def payment_confirm(request, id):
    context = {}
    user = request.user
    if user.is_teacher == True:
        Teacher = teacher.objects.get(username=user)
        context['Teacher'] = Teacher
        
    if Installments.objects.filter(id=id).exists():
        installment = Installments.objects.get(id=id)
        context['installment'] = installment
        student_id = installment.semester.Student.id
    
    if request.method == 'POST':
        name = request.POST['name']
        payment_method = request.POST['payment_method']
        a = installment.semester.Student.first_name+ ' '+ installment.semester.Student.last_name
        
        if a == name:
            # students =student.objects.get(id=student_id)
            # Sem = Semesters.objects.filter(Student=students)
            
            if payment_method == 'Cash':
                installment.is_paid = True
                installment.payment_method = payment_method
                installment.save()
                
                invoice = Invoice.objects.create(
                    student = installment.semester.Student,
                    semester = installment.semester,
                    installment = installment,
                    Invoice_id = random.randint(1111111111, 9999999999),
                    amount = installment.amount
                )
                invoice.save()
                
                messages.success(request, "Paid Recived Successfully!")
                return redirect(request.META['HTTP_REFERER'])
            
            elif payment_method == 'Bkash':
                amount = installment.amount
                name = installment.semester.Student.first_name+' '+installment.semester.Student.last_name
                email = installment.semester.Student.email
                phone_number = installment.semester.Student.phone_number
                address = installment.semester.Student.address
                product_name = installment.title
                product_category = installment.semester.title
                tran_id = installment.id
                data = {'amount': amount, 'name': name, 'email': email, 'phone_number': phone_number, 'address':address, 'product_name': product_name, 'product_category': product_category, 'tran_id': tran_id}
                
                return online_payment(data)
                
    return render(request, 'fees/payment_confirm.html', context)



def online_payment(data):
    settings = { 'store_id': 'ecomm654bdaf1131e9', 'store_pass': 'ecomm654bdaf1131e9@ssl', 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = data['amount']
    post_body['currency'] = "BDT"
    post_body['tran_id'] = data['tran_id']
    
    post_body['success_url'] = "http://127.0.0.1:8000/student/payment-success/"
    post_body['fail_url'] = "http://127.0.0.1:8000/student/payment-fail/"
    post_body['cancel_url'] = "your cancel url"
    
    post_body['emi_option'] = 0
    post_body['cus_name'] = data['name']
    post_body['cus_email'] = data['email']
    post_body['cus_phone'] = data['phone_number']
    post_body['cus_add1'] = data['address']
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = data['product_name']
    post_body['product_category'] = data['product_category']
    post_body['product_profile'] = "general"
    post_body['value_b'] = data['product_name']


    response = sslcommez.createSession(post_body)
    return redirect(response['GatewayPageURL'])


@csrf_exempt
def payment_success(request):
    post_body = request.POST
    print(post_body)
    id = post_body['tran_id']
    title = post_body['value_b']
    
    if title == 'Registrations Fees':
        registration = Registration_fees.objects.get(id=id)
        registration.is_paid = True
        registration.payment_method = 'Bkash'
        registration.save()
        
        invoice = Invoice.objects.create(
            student = registration.Student,
            semester = registration.semester,
            registration_fees = registration,
            Invoice_id = random.randint(1111111111, 9999999999),
            amount = registration.amount
        )
        invoice.save()
            
        messages.success(request, "Paid Recived Successfully!")
        return redirect('registration_fee_confirm', id=id)
    
    return redirect('online_payment_processing', id=id)

def online_payment_processing(request, id):
    Installment = Installments.objects.get(id=id)
    Installment.is_paid = True
    Installment.payment_method = 'Bkash'
    Installment.save()
    
    invoice = Invoice.objects.create(
        student = Installment.semester.Student,
        semester = Installment.semester,
        installment = Installment,
        Invoice_id = random.randint(1111111111, 9999999999),
        amount = Installment.amount
    )
    invoice.save()
          
    messages.success(request, "Paid Recived Successfully!")
    return redirect('payment_confirm', id=id)

@csrf_exempt
def payment_fail(request):
    post_body = request.POST
    Installment_id = post_body['tran_id']
    return redirect('payment_confirm', id=Installment_id)





@login_required(login_url='login')
def invoice(request, id):
    installment = Installments.objects.get(id=id)
    student_id = installment.semester.Student.id
    students =student.objects.get(id=student_id)
    # Sem = Semesters.objects.filter(Student=students)
    context = {'student': students, 'installment': installment}
            
            
    template_path = 'fees/fees_invoice.html'
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="installment_invoice.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
    # return render(request, 'fees/fees_invoice.html', context)
    # return render(request, 'fees/fees_invoice.html')
    
# ------------------------Fees Collection Section End----------------------------