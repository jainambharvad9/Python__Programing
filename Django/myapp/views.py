from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Service

def index(request):
    services = Service.objects.all()
    template = "index.html"
    return render(request, template, {"services": services})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = auth.authenticate(username=username_or_email, password=password)  # Note: 'username' should be used to authenticate

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Login failed')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk):
    return render(request, 'post.html',{'pk':pk})

def counters(request):
    posts = [1,2,3,4,5,'jainam','meet','nandan']
    return render(request, 'counter.html',{'posts':posts})
    