from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            print('login successfull ', request.user.first_name)
            print('user is login page : ', request.user.is_authenticate)
            return redirect('/module/')
        else:
            messages.error(request, 'Invalid credentials')
            print('Invalid credentials')
            return redirect('/')
        
    return render(request, 'login.html')

def module(request):
    return render(request, 'module.html')
