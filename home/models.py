from django.db import models

# Create your models here.

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

# class Articles(models.Model):
#     user = models.CharField(max_length=150, null=True)
#     titre_page = models.CharField(max_length=100, null=True, blank=True)
#     sous_titre_page = models.CharField(max_length=100, null=True, blank=True)
#     titres_articles = models.CharField(max_length=100)
#     sous_category_id = models.IntegerField(null=True, blank=True)
#     contenu = models.TextField()
#     image_path = models.ImageField(upload_to='articles/')
#     date_added = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.CharField(max_length=150, null=True, blank=True)
    name_article = models.CharField(max_length=150,null=True, blank=True)
    id_sous_category = models.IntegerField(null=True, blank=True)
    contenu = models.TextField()
    e_mail = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

class ArticleNote(models.Model):
    user = models.CharField(max_length=150, null=True, blank=True)
    name_article = models.CharField(max_length=150,null=True, blank=True)
    id_sous_category = models.IntegerField(null=True, blank=True)
    note_contenu = models.IntegerField()
    note_image = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)