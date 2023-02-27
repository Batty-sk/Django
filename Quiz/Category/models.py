from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.
class GK(models.Model):
    Question=models.CharField(max_length=200);
    Option1=models.CharField(max_length=100);
    Option2=models.CharField(max_length=100);
    Option3=models.CharField(max_length=100);
    Option4=models.CharField(max_length=100);
    Ans=models.CharField(max_length=100,null=True);

class Youtube(models.Model):
    Question=models.CharField(max_length=200);
    Option1=models.CharField(max_length=100);
    Option2=models.CharField(max_length=100);
    Option3=models.CharField(max_length=100);
    Option4=models.CharField(max_length=100);
    Ans=models.CharField(max_length=100,null=True);

class Sports(models.Model):
    Question=models.CharField(max_length=200);
    Option1=models.CharField(max_length=100);
    Option2=models.CharField(max_length=100);
    Option3=models.CharField(max_length=100);
    Option4=models.CharField(max_length=100);
    Ans=models.CharField(max_length=100,null=True);

class Maths(models.Model):
    Question=models.CharField(max_length=200);
    Option1=models.CharField(max_length=100);
    Option2=models.CharField(max_length=100);
    Option3=models.CharField(max_length=100);
    Option4=models.CharField(max_length=100);
    Ans=models.CharField(max_length=100,null=True);

class Geography(models.Model):
    Question=models.CharField(max_length=200);
    Option1=models.CharField(max_length=100);
    Option2=models.CharField(max_length=100);
    Option3=models.CharField(max_length=100);
    Option4=models.CharField(max_length=100);
    Ans=models.CharField(max_length=100,null=True);

class Science(models.Model):
    Question=models.CharField(max_length=200);
    Option1=models.CharField(max_length=100);
    Option2=models.CharField(max_length=100);
    Option3=models.CharField(max_length=100);
    Option4=models.CharField(max_length=100);
    Ans=models.CharField(max_length=100,null=True);