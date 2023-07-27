from django.urls import path
from . import views


from post import views as post_view


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

    #creating post url, only for admin
    path('post', post_view.create_post, name='cretae_post')
]