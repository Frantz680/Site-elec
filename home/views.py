from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import AddCategoryForm, AddCatForm
from .models import Sous_Category, Category

# Create your views here.



def home(request):
    """
    Show home page.
    """
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    return render(request, "home/index.html", {'sous_categorys': sous_categorys, "categorys": categorys})

def add(request, id_cat):
    """
    Show home page.
    """            
    

    if request.method == 'POST':
        print(id_cat)
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = AddCategoryForm()
    return render(request, "home/add_sous_category.html", {'form': form, 'id_cat': id_cat})

def add_cat(request):
    """
    Show home page.
    """
    if request.method == 'POST':
        form = AddCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = AddCatForm()
    return render(request, "home/add_cat.html", {'form': form})