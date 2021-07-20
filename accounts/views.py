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

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = UserProfileForm()

    return render(request, "accounts/my_account.html", {'form': form})
