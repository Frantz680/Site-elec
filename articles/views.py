from django.shortcuts import render

# Create your views here.


def home_tableau(request):
    """
    Display the 'legal notices' page.
    """

    return render(request, "tableau_elec/home_tableau.html")