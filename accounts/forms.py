from django import forms
from django.contrib.auth import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import UserProfile

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control', }))

    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }))


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control', }))

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', }))

    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }))

    password2 = forms.CharField(
    label='Confirmer le mot de passe :',
    widget=forms.PasswordInput(attrs={'class': 'form-control', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):

    avatar=forms.ImageField(
        label='Photo de profil :')

    class Meta:
        model = UserProfile
        fields = ['avatar']