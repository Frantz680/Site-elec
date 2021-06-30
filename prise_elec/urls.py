from django.urls import path

from prise_elec.views import home, beton, placo, garage

urlpatterns = [
    path('', home, name='home_prise'),
    path('placo', placo, name='placo'),
    path('beton', beton, name='beton'),
    path('garage', garage, name='garage'),
]