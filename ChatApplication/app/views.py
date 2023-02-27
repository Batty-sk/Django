from django.shortcuts import render
import threading
# Create your views here.
from .forms import Signup_login,Login_form,Upload_A_Image
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .client import Client
from .server import Server
from django.contrib.auth.models import User
from .models import User_pics
from django.contrib import messages
server_count=0;

def signup(req):
    if req.method=='POST':
        form=Signup_login(req.POST)
        if form.is_valid():
            print('is valid')
            user=form.save();
            login(req,user)
            default_pic=User_pics.objects.create(user=user,pic='/Profile_pics/random_guy.jpg')
            default_pic.save();
            return HttpResponseRedirect('/home/')
        else:
            print('is non valid')
            form.add_error('username','error')

    else:
        form=Signup_login();
    return render(req,'signup.html',{'form':form})

def Login(req):
    if req.method=="POST":
        form=Login_form(req,data=req.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user!=None:
                login(req,user)
                return HttpResponseRedirect('/home/')
            else:
                messages.error(req,'User Not Found !')
    else:
        form=Login_form(req)
    return render(req,'login.html',{'form':form});

def Logout(req):
    if not req.user.is_authenticated:
        logout(req)
    return HttpResponseRedirect('/login/')

def Home(req):
    global server_count;
    if req.user.is_authenticated:
        if req.method=='POST':
            form = Upload_A_Image(
            req.POST,
            req.FILES,
            instance=User_pics(user=req.user)
                )
            if form.is_valid():
                form.save();
                messages.success(req,'Successfully Uploaded!')
        else:
            form=Upload_A_Image();
        
        pic_url=User_pics.objects.get(user=req.user)
        print(pic_url.user.username)
        All_users=User_pics.objects.exclude(user=req.user);
   #     print(pic_url.pic.url)
        return render(req,'home.html',{'users':All_users,'form':form,'user_pic':pic_url})
    else:
        return HttpResponseRedirect('/login/')
        #connect the client to the server.