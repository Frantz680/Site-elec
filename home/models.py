from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, null=True)
    icon = models.ImageField(upload_to='icon_categorie/')


class Sous_Category(models.Model):
    category_id = models.IntegerField(null=True)
    name = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)


class PictureCarrousel(models.Model):
    picture = models.ImageField(upload_to='carrousel/')
    date_added = models.DateTimeField(auto_now_add=True)


class ArticleNote(models.Model):
    id_sous_category = models.IntegerField(null=True, blank=True)
    note_contenu = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


class Actualites(models.Model):
    nom_actu = models.CharField(max_length=150, blank=True, null=True)
    user = models.CharField(max_length=150, blank=True, null=True)
    contenu = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
