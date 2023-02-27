from django import forms
from .models import Employees

choicess=[
    (True,'Yes'),
    (False,'No')
]
class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields='__all__'
        widgets={'Date_of_joining':forms.widgets.DateInput(attrs={'type': 'date'}),'Phone':forms.TextInput(attrs={'class':'form-control w-70'}),'Married':forms.RadioSelect(choices=choicess),'Date_of_birth':forms.widgets.DateInput(attrs={'type': 'date'})}
    def clean_image(self):
        print('Validation')
        image = self.cleaned_data.get('Phone', False)  
        print(image)
            # validate image
        return None

class EmployeeSearchingForm(forms.Form):
    Id=forms.IntegerField(widget=forms.TextInput(attrs={'class':'small-field'}),required=False)
    Age=forms.IntegerField(max_value=100,widget=forms.TextInput(attrs={'class':'small-field'}),required=False)
    First_Name=forms.CharField(label='FirstName',max_length=100,required=False,widget=forms.TextInput(attrs={'class':'medium-field'}))
    Last_Name=forms.CharField(label='LastName',max_length=100,required=False,widget=forms.TextInput(attrs={'class':'medium-field'}))
    Phone=forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'large-field'}))
    Email=forms.EmailField(required=False,widget=forms.TextInput(attrs={'class':'large-field'}))
    State=forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class':'large-field'}))
    City=forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class':'large-field'}))
    Date_of_joining=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}),label='From Date [Joining]',required=False)
    ToDateOfJoining=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}),label='To Date [Joining]',required=False)
    Date_of_birth=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}),label='From Date [Dob]',required=False)
    ToDateOfBirth=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}),label='To Date [Dob]',required=False)
    Married=forms.CharField(max_length=10,widget=(forms.RadioSelect(choices=choicess)),required=False);

    Fetch_Multiple_records=forms.BooleanField(label='Fetch Multiple Records?',required=False)



