from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from accounts.forms import RegisterForm, UserProfileForm

from home.models import Sous_Category, Category
from home.views import request_user_avatar

# Create your views here.


def registrer_views(request):
    """
    User registration.
    :param request:
    :return: Direction to main page or register.
    """
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form, 'picture_user': picture_user, 
    'sous_categorys': sous_categorys, "categorys": categorys})

@login_required
def my_account_views(request):
    """
    Access to personal space.
    :param request:
    :return: Direction personal space with the products saved.
    """
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = UserProfileForm()

    return render(request, "accounts/my_account.html", {'form': form, 'picture_user': picture_user, 
    'sous_categorys': sous_categorys, "categorys": categorys})
