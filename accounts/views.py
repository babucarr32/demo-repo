from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST': #User has info and wants an an account
        if request.POST['password1']== request.POST['password2']:
            try:
                user= User.objects.get(username = request.POST['username'])
                return render(request,'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('login')
        else:
            return render(request, 'signup.html',{'error': 'Password nust match',})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST': #User has info and wants an an account
        user= auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('homePage')
        else:
            return render(request,'login.html', {'error': 'Username or Password is not correct'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST': #User has info and wants an an account
        auth.logout(request)
        return redirect('homePage')
