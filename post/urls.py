from django.urls import path
from . import views



urlpatterns = [
        path('', views.browse_homes, name='browse-homes'),
        
        # after a user browse a home they will e able to a detail for each home in the form of a modal popup
        # they chan schedule for a tour after selecting a specific home and they must be authenticated
]
