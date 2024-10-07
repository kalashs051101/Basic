from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# # Create your views here.
def email_to_client(request):
    send_mail(
        "this is subject",
        "this email is sent by django through email by kalash sharma",
        "kalashs051101@gmail.com",
        ["roshan_203036@saitm.org"],
        fail_silently=False,
    )
    return HttpResponse('successfully send')


#it is used for multi send email   
from django.core import mail
from django.http import HttpResponse
def multisend(request):
    connection = mail.get_connection()

    connection.open()
    reciever_list= ['kalash_203057@saitm.org']  #extend this list according to your requirement
    email1 = mail.EmailMessage('Hello', 'Body goes here', 'kalashs051101@gmail.com',
                            reciever_list, connection=connection)
    email1.send()
    connection.close()
    return HttpResponse('send')