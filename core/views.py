from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def home(request):
    context = {
        
    }
    return render(request, "core/home.html", context)


