from django.db import models
from account.models import student

# Create your models here.
class Semesters(models.Model):
    TITLE = (
        ('1st Semester', '1st Semester'),
        ('2nd Semester', '2nd Semester'),
        ('3rd Semester', '3rd Semester'),
        ('4th Semester', '4th Semester'),
        ('5th Semester', '5th Semester'),
        ('6th Semester', '6th Semester'),
        ('7th Semester', '7th Semester'),
        ('8th Semester', '8th Semester'),
        )
    Student = models.ForeignKey(student, on_delete=models.CASCADE, related_name="Students")
    title = models.CharField(choices=TITLE, max_length=50)
    start_date = models.DateField(auto_now_add=True)
    result = models.FloatField(max_length=5, blank=True, null=True)
    
    is_complete = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class Registration_fees(models.Model):
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Bkash', 'Bkash'),
        ('Others', 'Others'),
    )
    
    Student = models.ForeignKey(student, on_delete=models.CASCADE, related_name='Student')
    semester = models.ForeignKey(Semesters, on_delete=models.DO_NOTHING, related_name='Registration_fees_semester')
    
    title = models.CharField(max_length=50, default="Registrations Fees")
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    pay_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=15, blank=True, null=False)
    
    def __str__(self) -> str:
        return f'{self.Student} | {self.semester} | {self.title}'
    
    

class Installments(models.Model):
    TITLE = (
        ('1st Installment', '1st Installment'),
        ('2nd Installment', '2nd Installment'),
        ('3rd Installment', '3rd Installment'),
        ('4th Installment', '4th Installment'),
    )
    PAYMENT_METHOD = (
        ('Cash', 'Cash'),
        ('Bkash', 'Bkash'),
        ('Others', 'Others'),
    )
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, related_name="Semester")
    title = models.CharField(choices=TITLE, max_length=50)
    amount = models.PositiveIntegerField(default=3750)
    discount = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=15, blank=True, null=False)
    
    is_paid = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_date']
    

class Invoice(models.Model):
    student = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semesters, on_delete=models.DO_NOTHING, blank=True, null=True)
    installment = models.ForeignKey(Installments, on_delete=models.DO_NOTHING, blank=True, null=True)
    registration_fees = models.ForeignKey(Registration_fees, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    Invoice_id = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Invoice_id



