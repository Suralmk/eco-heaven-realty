from django.urls import path
from . import views



urlpatterns = [
       path('', views.admin_staff, name='adimn-staff'),
       path('add-home/' ,views.add_home, name='add-home'),

]