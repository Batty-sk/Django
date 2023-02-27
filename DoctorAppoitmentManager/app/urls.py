from django.urls import path
from .views import Home,find_emp

urlpatterns=[
    path('home/',Home,name='home'),
    path('Search_emp/',find_emp,name='search'),
]