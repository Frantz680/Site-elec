from django.db import models
from django.db.models.fields import CharField

from home.models import Category

# Create your models here.
# https://docs.djangoproject.com/fr/3.2/ref/forms/widgets/

class Comment(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
    Category, on_delete=models.CASCADE, default='1')
    e_mail = models.CharField(max_length=30)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    titre = models.CharField(max_length=100)
    category = models.ForeignKey(
    Category, on_delete=models.CASCADE, default='1')
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=100, default="/static/image/default/photo_a_venir.png")
