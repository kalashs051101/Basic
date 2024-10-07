from django.contrib import admin
from django.urls import path
from send_email_app2.views import *


urlpatterns = [
    path('email_to_client',email_to_client,name='email_to_client'),
    path('multisend',multisend,name='multisend')

    
]