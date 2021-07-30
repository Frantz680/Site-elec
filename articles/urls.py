from django.urls import path, include

from articles.views import view_articles, add_contenu_articles, add_title_articles

urlpatterns = [
    path('<slug:sous_category>/', view_articles, name='articles'),
    path('add_contenu_articles/<slug:sous_category_id>/', add_contenu_articles, name='add_contenu_articles'),
    path('add_title_articles/<slug:sous_category_id>/', add_title_articles, name='add_title_articles'),
]