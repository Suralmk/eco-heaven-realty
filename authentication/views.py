from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import messages
from .models  import *
from post.models import HomePost
from .helpers import forget_password_email_send, send_welcome_email, get_reset_email
User = get_user_model()

def base(request):
    return render(request, 'authentication/base.html')

def login(request):
    context = {
         'link' : 'http://127.0.0.1:8000/login/'
    }
    if request.user.is_authenticated:
        return redirect('base')
    if request.method == 'POST':
        print("some one is trying to login \n", request.POST)
        # storing the values entered by the user in a variable.
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)

        if auth_user == None:
            messages.info(request, "User not found")
        elif auth_user is not None:
            auth_login(request, auth_user)
            return redirect('base')
        else:
            return redirect('base')
    return render(request, 'authentication/login.html', context)

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
import uuid
def password_reset(request):
        if request.method == 'POST':
                email = request.POST['email']
        try:
            
                if not  User.objects.filter(email = email).first():
                    messages.info(request, "Email not found!")
                    
                else:  
                    #create a token
                    token = str(uuid.uuid4())
                    reciver = [email]
                    get_reset_email(email)
                    #saving the input email to profile table
                    profile_obj = Profile(forget_password_token = token, reset_email = email)
                    profile_obj.save()
                    forget_password_email_send(reciver, token)
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
    
    user_reset_email = Profile.objects.last()
    user_reset_email = user_reset_email.reset_email
    
    context = {
         'reset_email' : user_reset_email
    }
    return render(request, 'authentication/reset/email_sent_confirmation.html', context )

def create_password(request, token):
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        
    
        if request.method == 'POST':
            new_password = request.POST['new_password']
            if new_password == '' or None:
                 messages.info(request, "enter password")
            user_email = profile_obj.reset_email
            if User.objects.filter(email = user_email ).first():
                user_obj = User.objects.get(email=user_email)
                user_obj.set_password(new_password)
                user_obj.save()
                return redirect('reset-complete')

    except Exception as e:
         print(e)
    return render(request, 'authentication/reset/create_password.html')

def reset_complete(request):
    return render(request, 'authentication/reset/reset_complete.html')


#Anuthenticated user profile
def change_passwprd(request):
    
     return render(request, 'authentication/profile/change_password.html')

def search_post(request):
    try:
        if request.method == 'POST':
            searched = request.POST['searched']
            lowercase = HomePost.objects.first()
            print(lowercase)
            home = HomePost.objects.filter(city_location__icontains=searched)
           
    except Exception as e:
            print(e)
    return render(request, 'post/searched_homes.html', {'homes' : home})



#Admin views
def admin_staff(request):
     return render (request, 'authentication/admin.html')

     
     