from django.shortcuts import render
from .forms import Resume_Form
from django.http import HttpResponseRedirect
from .web_app import Resume_Generator
import os 

template_with_pictures=[2]
# Create your views here.
def Home(req):
    dir=os.listdir('L://Django//Django Projects//Resume_builder//static//template_screenshots');
    templates_with_nos={};
    count=1;
    for i in dir:
        templates_with_nos['template_screenshots//'+i]=count;
        count+=1;
    return render(req,'home.html',{'templates':templates_with_nos,'count':count});

def Fill_template(req,template_no=0):
    if(req.method=="POST"):
        about_yourself=Resume_Form.About_Yourself(req.POST)
        profile=Resume_Form.Profile_(req.POST)
        skills=Resume_Form.skills(req.POST)
        education=Resume_Form.Education(req.POST)
        projects=Resume_Form.Projects(req.POST)
        social_media=Resume_Form.Social_media(req.POST)
        experience=Resume_Form.experience(req.POST)
        print("template no",template_no)
        if template_no in template_with_pictures:
            flag=True;
        else:
            flag=0;
        if (about_yourself.is_valid() and skills.is_valid() and profile.is_valid() and skills.is_valid() and education.is_valid() and projects.is_valid() and social_media.is_valid() and experience.is_valid()):
            print(skills.cleaned_data['skill_1'])
            resume={'Name':f" {about_yourself.cleaned_data['Name']}",'jobtitle':about_yourself.cleaned_data['Job_title'],'234':f" {about_yourself.cleaned_data['Phone']} \t",'Il':f" {about_yourself.cleaned_data['Email']} \t",'In':f"{social_media.cleaned_data['Linkedin']}",
            'Er':f"{social_media.cleaned_data['Twitter']}",'profile':f" {profile.cleaned_data['Profile']} \t",
            'edu':[f"{education.cleaned_data['Education_1']}",f"{education.cleaned_data['Education_2']}",f"{education.cleaned_data['Education_3']}",f"{education.cleaned_data['Education_4']}"],'xp':[experience.cleaned_data['exp1'],experience.cleaned_data['exp2'],experience.cleaned_data['exp3'],experience.cleaned_data['exp4']],
            'ts':[f"{skills.cleaned_data['skill_1']}",f"{skills.cleaned_data['skill_2']}",f"{skills.cleaned_data['skill_3']}",f"{skills.cleaned_data['skill_4']}"],'lls':['Hardworking','CriticalThinking','Teamwork','Supportive'],
            '@Project':[f"{projects.cleaned_data['Project_1']}",f"{projects.cleaned_data['Project_2']}",f"{projects.cleaned_data['Project_3']}",f"{projects.cleaned_data['Project_4']}"]}
            if(Resume_Generator(resume,template_no,flag)):
                pass
            else:
                print("Success");
            #Polutting the data in word
            #after Polutting 
            return HttpResponseRedirect('/view_template/')
    else:
        about_yourself=Resume_Form.About_Yourself()
        profile=Resume_Form.Profile_()
        skills=Resume_Form.skills()
        education=Resume_Form.Education()
        projects=Resume_Form.Projects()
        social_media=Resume_Form.Social_media()
        experience=Resume_Form.experience()
    return render(req,'view_template.html',{'About_yourself':about_yourself,'Profile':profile,'Skills':skills,'Education':education,'Projects':projects,'exp':experience,'social_media':social_media})

def view_template(req):
    return render(req,'view_result.html');
