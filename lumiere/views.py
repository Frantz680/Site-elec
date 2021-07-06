from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import comment
from .models import Comment

# Create your views here.


def home(request):
    """
    Show home page.
    """
    comments = Comment.objects.all()
    return render(request, 'home_lumiere/index.html', {'comments':comments})


def interrupteur(request):
    """
    
    """

    return render(request, "home_lumiere/interrupteur.html")