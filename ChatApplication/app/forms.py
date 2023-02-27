from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import User_pics

class Signup_login(UserCreationForm):
    password2=None
    class Meta:
        model=User
        fields=['username']
        labels={'username':'Name','password1':'Password'}

    def Name_validator(self):
        value=self.cleaned_data['username']
        for i in value :
            try:
                val=int(i)
                raise forms.ValidationError('Field Contains The Number')
            except:
                pass;
        return value
class Login_form(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class Upload_A_Image(forms.ModelForm):
    class Meta:
        model=User_pics
        fields=['pic']
        labels={'pic':''}