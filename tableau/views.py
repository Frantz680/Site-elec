from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Show home page.
    """

    return render(request, "home_tableau/index.html")


def disjoncteur(request):
    """

    """

    return render(request, "home_tableau/disjoncteur.html")