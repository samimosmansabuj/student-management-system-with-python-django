from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=100)
    department_code  = models.PositiveIntegerField()
    established_date = models.DateTimeField(auto_now_add=True)
    HOD = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.title