from django.urls import path, include

from articles.views import view_articles, add_articles

urlpatterns = [
    path('<slug:sous_category>/', view_articles, name='articles'),
    path('add_articles/<slug:sous_category_id>/', add_articles, name='add_articles'),
]