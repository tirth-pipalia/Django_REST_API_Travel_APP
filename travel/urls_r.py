from django.urls import path
from .views import index,typography, about
urlpatterns = [
    path('',index,name='home'),
    path('typography.html',typography,name='typography'),
    path('about.html',about,name='about-us')
]