from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    
    return render(request, 'index')

def login(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'

    return render(request, 'login.html', {'form':form, 'msg': msg})


def register(request):
    msg = None

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            msg = 'Account created!'

            return redirect('login')
        else:
            msg = 'Invalid form'
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form':form, 'msg':msg})