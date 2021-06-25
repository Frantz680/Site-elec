from django.urls import path

from lumiere.views import home

urlpatterns = [
    path('', home, name='home_lumiere'),
]
