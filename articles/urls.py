from django.urls import path

from articles.views import home_tableau


urlpatterns = [
    path('tableau_elec/', home_tableau, name='home_tableau'),
]