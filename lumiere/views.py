from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import comment
from .models import Comment, Article

# Create your views here.


def home(request):
    """
    Show home page.
    """
    comments = Comment.objects.all()
    articles = Article.objects.all()

    if request.method == 'POST':
        form = comment(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = comment()
    return render(request, 'home_lumiere/index.html', {'form': form, 'comments': comments, 'articles': articles})


def interrupteur(request):
    """
    
    """

    return render(request, "home_lumiere/interrupteur.html")