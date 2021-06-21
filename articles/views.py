from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Show home page.
    """

    return render(request, "index.html")


def ml(request):
    """
    Display the 'legal notices' page.
    """

    return render(request, "mentions_legales.html")