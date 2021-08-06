from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms

from .models import PictureCarrousel, Sous_Category, Category, ArticleNote, FutureArticles, Improved


class AddCatForm(ModelForm):

    category = forms.CharField(
        label="Categorie",
        widget=forms.TextInput(attrs={'class': 'form-control' }))
    icon = forms.ImageField()

    class Meta:
        model = Category
        fields = ['category', 'icon']

class AddCategoryForm(ModelForm):

    category_id = forms.CharField(
        label="Id",
        widget=forms.TextInput(attrs={'class': 'form-control' }))

    name = forms.CharField(
        label="Nom de la sous-categorie",
        widget=forms.TextInput(attrs={'class': 'form-control' }))
        
    class Meta:
        model = Sous_Category
        fields = ['category_id', 'name']

class AddPictureCarrousel(ModelForm):

    picture = forms.ImageField()

    class Meta:
        model = PictureCarrousel
        fields = ['picture']

class addNoteArticleForm(ModelForm):

    id_sous_category = forms.CharField(
        label="id_sous_category",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)
    
    note_contenu = forms.CharField()

    class Meta:
        model = ArticleNote
        fields = [ 'id_sous_category', 'note_contenu']

class addFutureArticles(ModelForm):

    user = forms.CharField(        
        label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control' }))

    contenu = forms.CharField(
        label="Contenu sur les futurs articles",
        widget=forms.Textarea(attrs={'class': 'form-control' }))

    class Meta:
        model = FutureArticles
        fields = ['user', 'contenu']

class addImproved(ModelForm):

    user = forms.CharField(        
        label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control' }))

    contenu = forms.CharField(
        label="Contenu des améliorations",
        widget=forms.Textarea(attrs={'class': 'form-control' }))

    class Meta:
        model = Improved
        fields = [ 'user', 'contenu']