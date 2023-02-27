from django.urls import path
from . import views
urlpatterns=[
        path('Home/',views.Home,name='home'),
        path('User_details/<int:template_no>/',views.Fill_template,name='template'),
        path('view_template/',views.view_template),
]