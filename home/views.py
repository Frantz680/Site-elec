from django.shortcuts import render, redirect
# from django.contrib import messages

from accounts.models import UserProfile

from home.forms import AddCategoryForm, AddCatForm,\
    AddPictureCarrousel, ActualitesForm
from home.models import Sous_Category, Category, PictureCarrousel, Actualites


def request_user_avatar(request):
    """
    Query to retrieve user profile photo.
    """

    if request.user.is_authenticated:
        user = request.user
        user_avatars = UserProfile.objects.all()

        for user_avatar in user_avatars:

            if user_avatar.user_id == user.id:
                picture_user = user_avatar.avatar
                return picture_user
    else:
        picture_user = ""
        return picture_user


def home(request):
    """
    Show home page.
    """

    sous_categorys = Sous_Category.objects.all()
    categorys = Category.objects.all()

    actualites = Actualites.objects.all()[:5]

    pictures = PictureCarrousel.objects.all()

    picture_user = request_user_avatar(request)

    return render(request, "home/index.html",
                  {
                    'sous_categorys': sous_categorys,
                    'picture_user': picture_user,
                    "categorys": categorys,
                    "pictures": pictures,
                    "actualites": actualites
                  })


def ml(request):
    """
    Show mentions légales page.
    """

    sous_categorys = Sous_Category.objects.all()
    categorys = Category.objects.all()

    pictures = PictureCarrousel.objects.all()

    picture_user = request_user_avatar(request)

    return render(request, "home/ml.html",
                  {
                    'sous_categorys': sous_categorys,
                    'picture_user': picture_user,
                    "categorys": categorys,
                    "pictures": pictures
                  })


def add(request, id_cat):
    """
    Adding a category.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = AddCategoryForm()

    return render(request, "home/add_sous_category.html",
                  {
                    'form': form,
                    'picture_user': picture_user,
                    'id_cat': id_cat,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys
                  })


def add_cat(request):
    """
    Adding a sub-category.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':
        form = AddCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = AddCatForm()

    return render(request, "home/add_cat.html",
                  {
                    'form': form,
                    'picture_user': picture_user,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys
                  })


def add_picture_carrousel(request):
    """
    Adding a photo in the carousel.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':
        form = AddPictureCarrousel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPictureCarrousel()

    return render(request, "home/add_picture_carrousel.html",
                  {
                    'form': form,
                    'picture_user': picture_user,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys
                  })


def add_actu(request):
    """
    Adding information to the news.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()
    actualites = Actualites.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':
        form = ActualitesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActualitesForm()

    return render(request, "home/add_actu.html",
                  {
                    'form': form,
                    'picture_user': picture_user,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys,
                    "actualites": actualites
                  })


def all_actu(request):
    """
    View all news.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()
    actualites = Actualites.objects.all().order_by("-date_added")

    picture_user = request_user_avatar(request)

    return render(request, "home/all_actu.html",
                  {
                    'picture_user': picture_user,
                    'sous_categorys': sous_categorys,
                    'categorys': categorys,
                    'actualites': actualites
                  })
