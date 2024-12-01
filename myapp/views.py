from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:  # Redirect logged-in users
        return redirect('mapping')
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:  # Redirect logged-in users
        return redirect('mapping')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('mapping') 
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:  # Redirect logged-in users
        return redirect('mapping')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(username=email, password=password, first_name=name)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    return render(request, 'sign-up.html')

@login_required
def mapping(request):
    return render(request, 'mapping.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
