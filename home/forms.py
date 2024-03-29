# from django.db import models
# from django.db.models import fields
# from django.db.models.base import Model
from django.forms import ModelForm
from django import forms

from .models import PictureCarrousel, Sous_Category,\
    Category, ArticleNote, Actualites


class AddCatForm(ModelForm):

    category = forms.CharField(
        label="Categorie",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    icon = forms.ImageField()

    class Meta:
        model = Category
        fields = ['category', 'icon']


class AddCategoryForm(ModelForm):

    name = forms.CharField(
        label="Nom de la sous-categorie",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Sous_Category
        fields = ['category_id', 'name']


class AddPictureCarrousel(ModelForm):

    picture = forms.ImageField()

    class Meta:
        model = PictureCarrousel
        fields = ['picture']


class addNoteArticleForm(ModelForm):

    note_contenu = forms.CharField()

    class Meta:
        model = ArticleNote
        fields = ['sous_cat_id', 'note_contenu']


class ActualitesForm(ModelForm):

    CHOICES = [('1', 'Mises à jour'),
               ('2', 'Prochainement'),
               ('3', 'Important')]

    nom_actu = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    user = forms.CharField(
        label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    contenu = forms.CharField(
        label="Contenu sur les futurs articles",
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Actualites
        fields = ['nom_actu', 'user', 'contenu']
