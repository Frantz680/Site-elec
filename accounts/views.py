from accounts.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserProfileForm
# Create your views here.


def registrer_views(request):
    """
    User registration.
    :param request:
    :return: Direction to main page or register.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def my_account_views(request):
    """
    Access to personal space.
    :param request:
    :return: Direction personal space with the products saved.
    """

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
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = UserProfileForm()

    return render(request, "accounts/my_account.html", {'form': form, 'picture_user': picture_user})
