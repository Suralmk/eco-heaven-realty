from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]