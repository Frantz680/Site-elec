from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm
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
