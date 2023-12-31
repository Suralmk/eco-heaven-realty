from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import HomePost



User = get_user_model()


def browse_homes(request):
    postedHomes = HomePost.objects.all()
    
    context = {
        'homepost': postedHomes
    }
    return render(request, 'post/browse_homes.html', context)
