from django.urls import path
from . import views
urlpatterns=[path('quiz/<str:cat>',views.quiz,name='quiz'),
path('result/<str:cat>',views.show_result),
path('Home/',views.home,name='home'),]
