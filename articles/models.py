from django.db import models

# Create your models here.

class Title(models.Model):
    titre_page = models.CharField(max_length=100, null=True, blank=True)
    sous_titre_page = models.CharField(max_length=100, null=True, blank=True)
    sous_category_id = models.IntegerField(null=True, blank=True)

class Contenu(models.Model):
    user = models.CharField(max_length=150, null=True)
    titres_articles = models.CharField(max_length=100)
    sous_category_id = models.IntegerField(null=True, blank=True)
    contenu = models.TextField()
    image_path = models.ImageField(upload_to='articles/')
    date_added = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.CharField(max_length=150, null=True, blank=True)
    name_article = models.CharField(max_length=150,null=True, blank=True)
    id_sous_category = models.IntegerField(null=True, blank=True)
    contenu = models.TextField()
    e_mail = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)