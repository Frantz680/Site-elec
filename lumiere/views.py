from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Show home page.
    """

    return render(request, "home_lumiere/index.html")


def interrupteur(request):
    """
    
    """

    return render(request, "home_lumiere/interrupteur.html")