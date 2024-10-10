from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import LoginForm, RegistrationForm
from .models import *

# Home page
def home_view(request):
    return render(request, 'base.html')

# Sign up (registration) page
def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

# Login page
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

def profile_view(request):
    pass

def budget_view(request):
    pass

def savings_view(request):
    pass

def expenses_view(request):
    pass

def transactions_view(request):
    pass

def income_view(request):
    if request.user.is_authenticated:
        incomes = Income.objects.filter(user_id=request.user.id)
    else:
        return redirect('login')
    
    return render(request, 'income.html', {'incomes': incomes})


# @login_required
# def user_income_detail(request, income_id):
#     income = get_object_or_404(Income, id=income_id, user_id=request.user.id)
    
#     return render(request, 'income_detail.html', {'income': income})

#we could use login_required but aaah i do not like it
