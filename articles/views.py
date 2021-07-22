from django.shortcuts import render, redirect
from django.contrib import messages

from home.models import Sous_Category
from home.forms import Articles, addArticlesForm

# Create your views here.

def view_articles(request, sous_category):
    """
    Show home page.
    """
    
    sous_category = Sous_Category.objects.get(name=sous_category)
    articles = Articles.objects.filter(sous_category_id=sous_category.id)
    return render(request, "articles/detail.html", {"sous_category": sous_category, "articles": articles})

def add_articles(request, sous_category_id):
    """
    Show home page.
    """
    if request.method == 'POST':

        form = addArticlesForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addArticlesForm()
    return render(request, "articles/add_articles.html", {"sous_category_id": sous_category_id, 'form': form})

