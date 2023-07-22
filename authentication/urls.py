from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

    #password reset urls
    path('reset-password/', views.password_reset, name='reset_password'),
    path('email-sent-confirmation/', views.email_sent_confirmation, name='email-sent-confirmation'),
    path('create-password/', views.create_password, name='create-password'),
]