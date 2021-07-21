from django.db.models import fields
from django.forms import ModelForm
from django import forms

from .models import Articles, Sous_Category, Category


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

class addArticlesForm(ModelForm):

    user = forms.CharField()

    titre = forms.CharField()

    sous_category_id = forms.CharField()
    
    contenu = forms.CharField(
        label="Commentaire",
        widget=forms.Textarea(attrs={'class': 'form-control' }))

    image_path = forms.ImageField()

    class Meta:
        model = Articles
        fields = ['user', 'titre', 'sous_category_id', 'contenu', 'image_path']