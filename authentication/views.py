from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import messages
from .models  import *
from django.contrib.auth.models import auth
from .helpers import forget_password_email_send, send_welcome_email

User = get_user_model()

def base(request):
    return render(request, 'authentication/base.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('base')
    if request.method == 'POST':
        print("some one is trying to login \n", request.POST)
        # storing the values entered by the user in a variable.
        username = request.POST['username']
        password = request.POST['password']

        auth_user = authenticate(request, username=username, password=password)

        if auth_user == None:
            print("no one found\n")
        elif auth_user is not None:
            auth_login(request, auth_user)
            return redirect('base')
        else:
            return redirect('base')
    return render(request, 'authentication/login.html')

def logout(request):
    auth_logout(request)
    return redirect('base')

def signup(request):
    if request.method == 'POST':
        print("someone is trying to register\n")
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Please check ,Username already exist')
            return redirect("signup")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email was already Taken !')
            return redirect("signup")
        else:
            #send welcome email here before regestering the user
            email_context = {
                "first_name": first_name
            }
            subject = 'Welcome to Eco Heaven Realty'
            user_email = [email]
            send_welcome_email(request, subject, email_context, user_email )

            user = User.objects.create_user(
                                            username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            password=password,
                                            email=email )
            
            return redirect("base")
      
    return render(request, 'authentication/signup.html')

# Password reset
def password_reset(request):
        if request.method == 'POST':
                email = request.POST['email']
        try:
            
                if not  User.objects.filter(email = email).first():
                    messages.info(request, "Email not found!")
                    
                else:
                    reciver = [email]
                    forget_password_email_send(reciver)
                    return redirect('email-sent')
        except Exception as e:
            print(e)

        return render( request, 'authentication/reset/reset_password.html')


def email_sent_confirmation(request):
    """
    render email sent confirmation html template
    context : 
        'email' : key for the value
        reset_email : email of the user eho requested password recovery
    """

    return render(request, 'authentication/reset/email_sent_confirmation.html')

def create_password(request, token):
    try:
        #  profile_obj = Profile.objects.get(forget_password_token = token)
        #  print(profile_obj)
        print("")
    except Exception as e:
         print(e)
    return render(request, 'authentication/reset/create_password.html')

def reset_complete(request):
    return render(request, 'authentication/reset/reset_complete.html')