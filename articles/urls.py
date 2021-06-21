from django.urls import path

from articles.views import home, ml


urlpatterns = [
    path('', home, name='home'),
    path('mentions_legal/', ml, name='ml'),
]