from django.contrib import admin
from django.urls import path
from pdf.views import *



urlpatterns = [
    path('generate-pdf/',generate_pdf, name='generate_pdf'),
]
