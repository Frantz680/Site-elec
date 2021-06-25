from django.urls import path, include

from home.views import home

urlpatterns = [
    path('', home, name='home'),
    path('lumiere/', include('lumiere.urls')),
    path('prise/', include('prise_elec.urls')),
    path('tableau/', include('tableau.urls')),
]