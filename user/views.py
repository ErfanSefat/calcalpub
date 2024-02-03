from django.shortcuts import render

class logedinuser:
    fname = None
    lname = None
    username = None
signedin = logedinuser()
def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def signOut(request):
    return render(request, "home.html")

def addevent(request):
    return render(request, "addevent.html")


def addschedule(request):
    return render(request, "addschedule.html")

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse
from .models import student
from django.contrib import messages

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
            signedin.fname = user.fname
            signedin.lname = user.lname
            signedin.username = user.username
            print(signedin)
            print("Yyooyoyooyoy")
            return redirect('http://127.0.0.1:8000/success')
        # user = authenticate(request, username=username, password=password)
        # print(user)

        # if user is not None:
        #     login(request, user)
        #     print("Authentication successful!")
        # else:
        #     print("Authentication failed.")

    return render(request, 'signin.html')

