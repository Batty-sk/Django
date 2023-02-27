from django import forms


def check_for_no(value):
    for i in value:
        print(i)
        return forms.ValidationError('Please Enter The Valid Food Items')

class CalorieCalc(forms.Form):
    food1=forms.CharField(max_length=100,required=True,help_text='Make sure The spelling of the food is correct',validators=[check_for_no]);
