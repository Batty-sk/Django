from django.contrib import admin
from .models import Employees
# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    list_display=['id','First_Name','Last_Name','Email','Phone','Married','Age','Date_of_joining','Department']


admin.site.register(Employees,AdminEmployee)