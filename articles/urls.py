from django.urls import path

from articles.views import home_tableau, home


urlpatterns = [
    path('', home, name='home'),
    path('tableau_elec/', home_tableau, name='home_tableau'),
]