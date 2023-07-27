from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
import sys
sys.path.append("..")


User = get_user_model()

def create_post(request):
    return render(request, 'post/create_post.html')