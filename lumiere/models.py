from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=30)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
