from django.shortcuts import render

# Create your views here.
from .forms import EmployeeRegistrationForm,EmployeeSearchingForm
from .models import Employees
from django.db.models import Q

def Home(req):
    if req.method=='POST':
        form=EmployeeRegistrationForm(req.POST)
        if form.is_valid():
            form.save();
            print('saved Successfully ')
    else:
        form=EmployeeRegistrationForm()
    return render(req,'Home/Home.html',{'form':form})

def find_emp(req):
    Emp=[]
    if req.method=="POST":
        form=EmployeeSearchingForm(req.POST)
        if form.is_valid():
            try:
                Employee=Employees.objects.get(pk=form.cleaned_data['Id'])
                Emp.append(Employee);
            except:
                if form.cleaned_data['Fetch_Multiple_records']:
                    objects=Employees.objects.filter(Q(First_Name=form.cleaned_data['First_Name']) | Q(Last_Name=form.cleaned_data['Last_Name']))
                    for o in objects:
                        Emp.append(o)
                else:

                    object=Employees.objects.filter( Q(First_Name=form.cleaned_data['First_Name']) & Q(Last_Name=form.cleaned_data['Last_Name'])).first();
                    Emp.append(object);

    else:

        form=EmployeeSearchingForm()
    print(Emp);
    return render(req,'Home/Find_emp.html',{'form':form,'Emp':Emp});