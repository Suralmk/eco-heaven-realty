from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import messages
# from django.core.mail import send_mail , EmailMessage
# from django.template.loader import render_to_string
# from django.conf import settings #imported setting to get the sender email EMAIL_HOST_USER
from django.contrib.auth.models import auth
from . import helpers


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

# def send_email( request, subject, email_context, recipient_list):
#     """
#     Send an email from the sign up page
#         request: responce of the form
#         subject: subject of the email
#         email_context:
#             key: used in the html template for rendering data from the database
#             value: the data
#         recipient_list: List of email, to send email
#     """

#     #in order to use this function for sending emails for diffrent purpose, this html_tempate has to be changed
#     html_template = 'authentication/email_templates/welcome.html'
    
#     html_message = render_to_string(html_template, context=email_context)
    
#     email_from = settings.EMAIL_HOST_USER

#     # send_mail(subject, html_message,email_from, recipient_list, fail_silently=False)
#     message = EmailMessage(subject, html_message,
#                             email_from, recipient_list)
#     message.content_subtype = 'html'
#     message.send()
#     return render(request, 'authentication/signup.html')

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
            helpers.send_welcome_email(request, subject, email_context, user_email )

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
        reciver = [email]
        helpers.forget_password_email_send(request,reciver)

    return render( request, 'authentication/reset/reset_password.html')

def email_sent_confirmation(request):
    return render(request, 'authentication/reset/email_sent_confirmation.html')

def create_password(request):
    return render(request, 'authentication/reset/create_password.html')