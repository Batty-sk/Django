from django.db import models

# Create your models here.
Departments=(
('Sales Department','Sales Department')
,('IT Department','IT Department'),
('Production Department','Production Department')
)

class Employees(models.Model):
    First_Name=models.CharField(max_length=100,null=False)
    Last_Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Married=models.CharField(max_length=10);
    Age=models.IntegerField()
    State=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Date_of_joining=models.DateField()
    Date_of_birth=models.DateField()
    Department=models.CharField(max_length=200,choices=Departments,default='Sales Department')
