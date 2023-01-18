# from django.contrib import admin
from django.contrib import admin

from .models import Category, Sous_Category, PictureCarrousel, ArticleNote

admin.site.register(Category)

admin.site.register(Sous_Category)

admin.site.register(PictureCarrousel)

admin.site.register(ArticleNote)