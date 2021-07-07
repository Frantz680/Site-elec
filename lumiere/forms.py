from django import forms

# Create your models here.

class comment(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            )
        )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            )
        )
        
    comment = forms.CharField(
        max_length=1000, 
        label="Commentaire",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            )
        )
