from django.urls import path

from prise_elec.views import home

urlpatterns = [
    path('', home, name='home_prise'),
]