# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'sign-up.html')

def mapping(request):
    return render(request, 'mapping.html')