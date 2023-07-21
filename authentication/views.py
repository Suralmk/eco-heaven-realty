from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def base(request):
    return render(request, 'authentication/base.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('base')
    print(request.user.is_authenticated)

    return render(request, 'authentication/login.html')
def signup(request):
    return render(request, 'authentication/signup.html')