from django.urls import path
from . import views



urlpatterns = [
        path('', views.browse_homes, name='browse-homes'),
       #

]