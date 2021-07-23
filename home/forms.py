from django.db.models import fields
from django.forms import ModelForm
from django import forms

from .models import Articles, Sous_Category, Category, Comment


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

    titre_page = forms.CharField(
        label="Titre de la page",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    sous_titre_page = forms.CharField(
        label="Sous titre de la page",
        widget=forms.TextInput(attrs={'class': 'form-control' }),
        strip=False,
        required=False)

    titres_articles = forms.CharField(
        label="Titre de l'article",
        widget=forms.TextInput(attrs={'class': 'form-control' }))

    sous_category_id = forms.CharField()
    
    contenu = forms.CharField(
        label="Commentaire",
        widget=forms.Textarea(attrs={'class': 'form-control' }))

    image_path = forms.ImageField()

    class Meta:
        model = Articles
        fields = ['user', 'titre_page', 'sous_titre_page', 'titres_articles', 'sous_category_id', 'contenu', 'image_path']

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
