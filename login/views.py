from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *

def home(request):
    if request.user.is_authenticated:
        data = {
            "user": request.user
        }
        return render(request, 'home.html', data)
    return redirect('/')

def registerview(request):
    if request.method == "POST" and request.POST.get('p') == request.POST.get('cp'):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        return redirect('/')
    return render(request, 'register.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('l'),
            password=request.POST.get('p'),
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect('/home/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')