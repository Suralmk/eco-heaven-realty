from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

    path('reset-password/', views.password_reset, name='reset_password'),
    path('email_sent_confirmation/', views.email_sent_confirmation, name='email_sent_confirmation'),
]