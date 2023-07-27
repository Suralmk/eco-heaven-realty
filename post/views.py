from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import HomePost
from authentication.templates.authentication import  *


User = get_user_model()

def create_post(request):
    postedHomes = HomePost.objects.all()
    
    context = {
        'homepost': postedHomes
    }
    return render(request, 'post/create_post.html', context)
def search_post(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_homes = HomePost.objects,filter(city__containes=searched)

        context = {
            'searched_homes':searched_homes
        }
        return render(request, 'post/seaarched_homes.html' )