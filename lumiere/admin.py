from django.contrib import admin

from .models import Comment, Article

# Register your models here.

admin.site.register(Comment)
admin.site.register(Article)