from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django import forms

from .models import PictureCarrousel, Sous_Category, Category, Comment, ArticleNote


class AddCatForm(ModelForm):
    category = forms.CharField()
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

class addCommentForm(ModelForm):

    user = forms.CharField(        
        label="user",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    name_article = forms.CharField(
        label="id_article",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    id_sous_category = forms.CharField(
        label="id_sous_category",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    e_mail = forms.CharField()
    
    contenu = forms.CharField(
        label="Commentaire",
        widget=forms.Textarea(attrs={'class': 'form-control' }))

    class Meta:
        model = Comment
        fields = ['user', 'name_article', 'id_sous_category', 'e_mail', 'contenu']

class addNoteArticleForm(ModelForm):

    user = forms.CharField(        
        label="user",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    name_article = forms.CharField(
        label="id_article",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    id_sous_category = forms.CharField(
        label="id_sous_category",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    note_contenu = forms.CharField()
    
    note_image = forms.CharField(
        label = {'note': 'Note /5'},
        widget=forms.NumberInput(attrs={'class': 'Stars'}))

    class Meta:
        model = ArticleNote
        fields = ['user', 'name_article', 'id_sous_category', 'note_contenu', 'note_image']
 
