from email import message
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .models import GK,Youtube,Sports,Science,Maths,Geography
score=0;
quiz_models={'gk':GK,'youtube':Youtube,'sports':Sports,'science':Science,'maths':Maths,'geography':Geography}
def quiz(req,cat):
    global score;
    if(req.method=='POST'):
        count=1;
        quest_count=0;
        while(quest_count<10):
            ans=req.POST.get(str(count),'0')
            if(ans!='0'):
                question=quiz_models[cat].objects.get(id=count);
                quest_count+=1;
                if ans=='':
                    messages.warning(req,'Please Attempt All The Questions');
                    return HttpResponseRedirect(f'/quiz/{cat}')
                if question.Ans==ans:
                    score+=1;
                    #print('you won a score');
            count+=1;
        response=HttpResponseRedirect(f'/result/{cat}');
        scr=req.COOKIES.get('score');
        if scr==None:
            response.set_cookie('score',score);
        else:    
            if int(scr)<score:
                response.set_cookie('score',score);
                response.set_cookie('message','Congrats You have done Improvement');
            else:  
                response.set_cookie('score',score);
        score=0;    
        return response;
    quizs=quiz_models[cat].objects.all();
    return render(req,'Quiz.html',{'quiz':quizs,'category':cat});


def show_result(req,cat):
    score=req.COOKIES.get('score');
    msg=req.COOKIES.get('message');
    messages.success(req,'Congratulations On Completing The Test');
    return render(req,'show_result.html',{'score':score,'msg':msg,'cat':cat})

def home(req):
    res=render(req,'home.html');
    res.delete_cookie('score')
    res.delete_cookie('message')
    return res