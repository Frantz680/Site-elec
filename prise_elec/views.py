from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Show home page.
    """

    return render(request, "home_prise/index.html")

def placo(request):
    """
    Show home page.
    """

    return render(request, "home_prise/placo.html")

def encastrement(request):
    """
    Show home page.
    """

    return render(request, "home_prise/encastrement.html")

def garage(request):
    """
    Show home page.
    """

    return render(request, "home_prise/garage.html")