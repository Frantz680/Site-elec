from django.urls import path

from prise_elec.views import home, encastrement, placo, garage

urlpatterns = [
    path('', home, name='home_prise'),
    path('placo', placo, name='placo'),
    path('encastrement', encastrement, name='encastrement'),
    path('garage', garage, name='garage'),
]