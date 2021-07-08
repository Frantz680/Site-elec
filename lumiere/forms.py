from django.db.models import fields
from django.forms import ModelForm
from django import forms

from .models import Comment

# Create your models here.

class CommentForm(ModelForm):
    name = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control' }))

    e_mail = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(attrs={'class': 'form-control' }))

    body = forms.CharField(
        label="Commentaire",
        widget=forms.Textarea(attrs={'class': 'form-control' }))

    class Meta:
        model = Comment
        fields = ['name', 'e_mail', 'body']
