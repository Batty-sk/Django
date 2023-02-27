from django import forms
#
#CHOICES = [('Male','Male'),('Female','Female')]

class Resume_Form(forms.Form):
    class About_Yourself(forms.Form):
        Name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'value'}));
        Job_title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'value'}));
        #Age=forms.CharField(max_length=20);
        Email=forms.EmailField(widget=forms.TextInput(attrs={'class':'value'}));
        #Nationality=forms.CharField(max_length=100,required=False);
        Phone=forms.IntegerField(widget=forms.TextInput(attrs={'class':'value'}));

    class experience(forms.Form):
        exp1=forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class':'value'})) 
        exp2=forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class':'value'}))  
        exp3=forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class':'value'}))  
        exp4=forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class':'value'}))  

    #skills 
    class Profile_(forms.Form):
        Profile=forms.CharField(widget=forms.Textarea())

    class skills(forms.Form):
        skill_1=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'value'}))
        skill_2=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'value'}))
        skill_3=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'value'}))
        skill_4=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'value'}))
    #Education section 
    class Education(forms.Form):
        Education_1=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
        Education_2=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
        Education_3=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
        Education_4=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));

    #Projects
    class Projects(forms.Form):
        Project_1=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
        Project_2=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
        Project_3=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
        Project_4=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}));
    #Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES));

    #socila media links
    class Social_media(forms.Form):    
        Linkedin=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}))
        Twitter=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'value'}))


#class Profile(forms.Form):



