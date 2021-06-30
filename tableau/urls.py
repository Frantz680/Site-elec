from django.urls import path

from tableau.views import home, disjoncteur

urlpatterns = [
    path('', home, name='home_tableau'),
    path('disjoncteur', disjoncteur, name='disjoncteur'),
]
