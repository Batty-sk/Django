from django.contrib import admin
from .models import GK,Sports,Youtube,Maths,Geography,Science
# Register your models here.
class base(admin.ModelAdmin):
    list_display=['Question','Option1','Option2','Option3','Option4','Ans']
admin.site.register(GK,base);
admin.site.register(Sports,base);
admin.site.register(Youtube,base);
admin.site.register(Maths,base);
admin.site.register(Geography,base);
admin.site.register(Science,base);