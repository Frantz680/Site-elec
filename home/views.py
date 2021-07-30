from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from accounts.models import UserProfile
from .forms import AddCategoryForm, AddCatForm, AddPictureCarrousel
from .models import Sous_Category, Category, PictureCarrousel

# Create your views here.


def home(request):
    """
    Show home page.
    """
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()
    pictures = PictureCarrousel.objects.all()

    user = request.user
    user_avatars = UserProfile.objects.all()

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    return render(request, "home/index.html", {'sous_categorys': sous_categorys, 'picture_user': picture_user,
     "categorys": categorys, "pictures": pictures})

def add(request, id_cat):
    """
    Show home page.
    """            

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    user = request.user
    user_avatars = UserProfile.objects.all()

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = AddCategoryForm()
    return render(request, "home/add_sous_category.html", {'form': form, 'picture_user': picture_user, 'id_cat': id_cat, 'sous_categorys': sous_categorys, "categorys": categorys})

def add_cat(request):
    """
    Show home page.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    user = request.user
    user_avatars = UserProfile.objects.all()

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    if request.method == 'POST':
        form = AddCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = AddCatForm()
    return render(request, "home/add_cat.html", {'form': form, 'picture_user': picture_user,
     'sous_categorys': sous_categorys, "categorys": categorys})

def add_picture_carrousel(request):

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    user = request.user
    user_avatars = UserProfile.objects.all()

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    if request.method == 'POST':
        form = AddPictureCarrousel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPictureCarrousel()
    return render(request, "home/add_picture_carrousel.html", {'form': form, 'picture_user': picture_user,
     'sous_categorys': sous_categorys, "categorys": categorys})