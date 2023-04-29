from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from Auth.models import Test
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# login


def login(request):
    return render(request, 'Auth/login.html')


def loging(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = None
    if request.method == "POST":
        try:
            user = Test.objects.get(email=email)
            print(user)
        except Test.DoesNotExist:
            user = None
            print(user)
        if user is not None and check_password(password, user.password):
            print(user)
            # login(request, user)
            return redirect('user')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'Auth/login.html')


def signup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = make_password(password)
    user = Test.objects.create(name=name, email=email, password=password)
    if user is not None:
        return HttpResponse('User created successfully')
    else:
        return HttpResponse('An Error occured')


# logout
@login_required(login_url="login")
def logout(request):
    logout(request)
    return redirect('login')
