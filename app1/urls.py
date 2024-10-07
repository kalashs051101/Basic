from django.contrib import admin
from django.urls import path
from app1.views import *


urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('read/',read,name='read'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('login',loginn,name='loginn'),
]