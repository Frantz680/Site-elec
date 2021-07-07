from django.db.models import fields
from django.forms import ModelForm
from .models import Comment

# Create your models here.

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'e_mail', 'body']
