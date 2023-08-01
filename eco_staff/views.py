from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from post.models import HomePost
from django.contrib.auth import get_user_model
User = get_user_model()



#Admin views
#each one of those views should have a token in their url
def admin_staff(request):
     if not request.user.is_staff:
         return redirect('base')
     else:
        return render (request,'eco_staff/admin.html')

def add_home(request):
    if not request.user.is_staff:
         return redirect('base')
    else:

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

def see_users(request):
    if not request.user.is_staff:
         return redirect('base')
   
    users = User.objects.all()
    
    if request.method == 'POST':
            searched_user = request.POST['searched']
            print(searched_user)
            try:
               searched =  users.filter(username__icontains=searched_user).values()
               print(searched)
            except Exception as e:
                print('no')
    context = {
            'users': users,
            'searched_user': searched
        }
    return render(request, 'eco_staff/registered_users.html', context)
    
    
def delete_users(request):
    if not request.user.is_staff:
         return redirect('base')
    else:
        return render(request, 'eco_staff/delete_users.html' )

def delete_homes(request):
    if not request.user.is_staff:
         return redirect('base')
    else:
        return render(request, 'eco_staff/delete_homes.html' )

def tour_requests(request):
    if not request.user.is_staff:
         return redirect('base')
    else:
        return render(request, 'eco_staff/tour_requests.html' )