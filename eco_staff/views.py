from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from post.models import HomePost




#Admin views
def admin_staff(request):
     return render (request,'eco_staff/admin.html')

def add_home(request):
    if request.method == 'POST':
        city_location = request.POST['city_location']
        home_location = request.POST['home_location']
        home_type = request.POST['home_type']
        bed_rooms = request.POST['bed_rooms']
        bath_rooms = request.POST['bath_rooms']
        sqft = request.POST['sqft']
        price = request.POST['price']
        image = request.FILES['image']
        try:
            Home = HomePost(
                city_location=city_location,
                home_location=home_location,
                home_type=home_type,
                beds_rooms=bed_rooms,
                bath_rooms=bath_rooms,
                sqft=sqft,
                price=price,
                image=image
            )
            Home.save()
            messages.info(request, "Succesfully added a home")
        except Exception as e:
            print(e)
    return render(request, 'eco_staff/add_home.html')