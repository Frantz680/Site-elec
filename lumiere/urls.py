from django.urls import path

from lumiere.views import home, interrupteur

urlpatterns = [
    path('', home, name='home_lumiere'),
    path('interrupteur', interrupteur, name='interrupteur'),
]
