from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_pics(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    pic=models.ImageField(upload_to='Profile_pics')