from django.urls import path, include

from articles.views import view_articles

urlpatterns = [
    path('<slug:sous_category>/', view_articles, name='articles'),
]