from django.contrib import admin
from .models import User_pics
# Register your models here.

class Show_user_pics(admin.ModelAdmin):
    list_display=['user','pic']

admin.site.register(User_pics,Show_user_pics)
