from django.shortcuts import render,redirect
from app1.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return HttpResponse('this is home page')


def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        roll=request.POST['roll']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1==pass2:
            data=student.objects.create(name=name,age=age,roll=roll,email=email,pass1=pass1,pass2=pass2)
            data.save()
            return HttpResponse('saved')
        else:
            return HttpResponse('failed')
    return render(request,'create.html')

def read(request):
    data = student.objects.all()

    return render(request,'read.html',{'data':data})

def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        roll=request.POST['roll']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        student.objects.filter(id=id).update(name=name,age=age,roll=roll,email=email,pass1=pass1,pass2=pass2)
        return redirect('read')
    obj=student.objects.get(id=id)
    return render(request,'update.html',{'obj':obj})

def delete(request,id):
    obj = student.objects.get(id=id)
    obj.delete()

    return HttpResponse('deleted')


def loginn(request):
    if request.method == "POST":
        nname=request.POST['name']
        ppass1=request.POST['pass1']

        user = authenticate(name=nname,pass1=ppass1)

        if user is not None:
            login(request,user)
            return redirect('read')
        else:
            return HttpResponse('invalid....first register yourself ')
    return render(request,'login.html')