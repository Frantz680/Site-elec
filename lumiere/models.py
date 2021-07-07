from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=30)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=100, default="Null")
