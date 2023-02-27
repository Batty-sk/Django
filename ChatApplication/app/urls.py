from django.urls import path
from .views import Home,signup,Login,Logout
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('home/',Home,name='home'),
    path('login/',Login,name='login'),
    path('signup/',signup,name='singup'),
    path('logout/',Logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)