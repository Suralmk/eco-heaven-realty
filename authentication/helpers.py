from django.core.mail import send_mail , EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import uuid
from django.conf import settings #imported setting to get the sender email EMAIL_HOST_USER

def send_welcome_email( request, subject, email_context, recipient_list):
    """
    Send an email from the sign up page
        request: responce of the form
        subject: subject of the email
        email_context:
            key: used in the html template for rendering data from the database
            value: the data
        recipient_list: List of email, to send email
    """
    #in order to use this function for sending emails for diffrent purpose, this html_tempate has to be changed
    html_template = 'authentication/email_templates/welcome.html'
    
    html_message = render_to_string(html_template, context=email_context)
    
    email_from = settings.EMAIL_HOST_USER

    # send_mail(subject, html_message,email_from, recipient_list, fail_silently=False)
    message = EmailMessage(subject, html_message,
                            email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
    return render(request, 'authentication/signup.html')

def forget_password_email_send(request, recipient_list):
    """
    Send an email from the sign up page
        request: responce of the form
        subject: subject of the email
        email_context:
            key: used in the html template for rendering data from the database
            value: the data
        recipient_list: List of email, to send email
    """
    token = str(uuid.uuid4())
    # token_message  = f'http://127.0.0.1:8000/create-password/{token}/'
    subject = "Password Recovery, Eco Heaven Realty"
    html_template = 'authentication/email_templates/password_reset_email.html'
    email_context = {
        'token_key': f'http://127.0.0.1:8000/create-password/{token}/'
    }
    html_message = render_to_string(html_template, context=email_context)
    
    email_from = settings.EMAIL_HOST_USER

    # send_mail(subject, html_message,email_from, recipient_list, fail_silently=False)
    message = EmailMessage(subject, html_message,
                            email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
    return render( request, 'authentication/reset/reset_password.html')