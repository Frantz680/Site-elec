from django.urls import path

from tableau.views import home

urlpatterns = [
    path('', home, name='home_tableau'),
]
