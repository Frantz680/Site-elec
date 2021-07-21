from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, null=True)
    icon = models.ImageField(upload_to='icon_categorie/')

class Sous_Category(models.Model):
    category_id = models.IntegerField(null=True)
    name = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

class Articles(models.Model):
    user = models.CharField(max_length=150, null=True)
    titre = models.CharField(max_length=100)
    sous_category_id = models.IntegerField(null=True, blank=True)
    contenu = models.TextField()
    image_path = models.CharField(max_length=100, default="/static/image/default/photo_a_venir.png")
    date_added = models.DateTimeField(auto_now_add=True)