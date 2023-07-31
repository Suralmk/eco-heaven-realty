from django.urls import path, include 
from . import views
from eco_staff.urls import urlpatterns as eco_url
from eco_staff.views import admin_staff as  eco_admin

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    #password reset urls
    path('reset-password/', views.password_reset, name='reset_password'),
    path('email-sent/', views.email_sent_confirmation, name='email-sent'),
    path('create-password/<token>/', views.create_password, name='create-password'),
    path('reset-complete/', views.reset_complete, name='reset-complete'),

    #Authenticated user profile urls
    path('change-password/', views.change_passwprd, name='change_passwprd'),

    # Searching a post every one can search
    # no need to login, signup, be an admin
    path('searched-post/', views.search_post, name='searched-post'),
    path("admin-staff/", eco_admin, name='admin-staff')
    
]