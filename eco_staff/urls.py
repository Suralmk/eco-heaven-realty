from django.urls import path
from . import views



urlpatterns = [
       path('', views.admin_staff, name='adimn-staff'),
       path('add-home/' ,views.add_home, name='add-home'),
       path('users/' ,views.see_users, name='users'),
       path('delete-users/' ,views.delete_users, name='delete-users'),
       path('delete-homes/' ,views.delete_homes, name='delete-homes'),
       path('tour-requests/' ,views.tour_requests, name='tour-requests'),

]