from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse
from .models import student, event
from django.contrib import messages
from django.template import loader
from json import dumps 
from django.core import serializers


def home(request):
    try:
        usersevent = event.objects.filter(input_username=myuserobj)
        events = serializers.serialize('json', usersevent)
        userdata = dumps(userpass)
        return render(request, 'home.html', {'userdata': userdata, 'events': events})
    except:
        return redirect("http://127.0.0.1:8000")

def success(request):
    return render(request, 'success.html')

def signOut(request):
    return render(request, "home.html")

def addevent(request):
    if request.method == 'POST':
        input_year = request.POST.get('input_year')
        input_month = request.POST.get('input_month')
        input_day = request.POST.get('input_day')
        input_text = request.POST.get('text')
        input_time = request.POST.get('time')
        makeevent = event(input_username = myuserobj, input_year=input_year, input_month=input_month, input_day=input_day, input_text=input_text, input_time=input_time)
        makeevent.save()
    userdata = dumps(userpass)
    return render(request, 'addevent.html', {'userdata': userdata})


def addschedule(request):
    return render(request, "addschedule.html")

def signup(request):    
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('StuNum')
        password = request.POST.get('password')
        user = student(username = username, password = password, fname = fname, lname = lname)
        try:
            user.save()
            return redirect('http://127.0.0.1:8000/signin/')
        except:
            messages.info(request, '.این نام‌کاربری در سیستم وجود دارد')

    return render(request, 'signup.html')

def signin(request):
    global myuserobj
    myuserobj = None
    if request.method == 'POST':
        username = request.POST.get("StuNum")
        password = request.POST.get("password")
        
        try:
            user = student.objects.get(username=username)
        except student.DoesNotExist:
            user = None

        if user.password != password:
            messages.info(request, '.این نام‌کاربری با این رمزعبور همخوانی ندارد')
        else:
            myuserobj = username
            global userpass
            userpass = dict(fname=user.fname, lname=user.lname, username=user.username)
            return redirect('http://127.0.0.1:8000/home')
    return render(request, 'signin.html')