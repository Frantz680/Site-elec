from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import UserProfile

from home.models import Sous_Category, Category
from home.forms import addNoteArticleForm

from articles.models import Contenu, Title, Comment
from articles.forms import addContenuArticlesForm, addTitleArticlesForm, addCommentForm

from .my_captcha import FormWithCaptcha

# Create your views here.

def view_articles(request, sous_category):
    """
    Show home page.
    """    

    comments = Comment.objects.all()
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()
    user_avatars = UserProfile.objects.all()

    sous_category = Sous_Category.objects.get(name=sous_category)
    title_articles = Title.objects.filter(sous_category_id=sous_category.id) 
    contenu_articles = Contenu.objects.filter(sous_category_id=sous_category.id)
    
    user = request.user

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    if request.method == 'POST':

        form_note = addNoteArticleForm(request.POST)

        if form_note.is_valid():
            
            form_note.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form_note = addNoteArticleForm()

    if request.method == 'POST':

        form = addCommentForm(request.POST)


        if form.is_valid():
            
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    
    else:
        form = addCommentForm()

    return render(request, "articles/detail.html", {"sous_category": sous_category, 'picture_user': picture_user, "title_articles": title_articles,
    "contenu_articles": contenu_articles, 'sous_categorys': sous_categorys, "categorys": categorys, "form": form, "comments": comments,
    "captcha": FormWithCaptcha, "form_note": form_note,})

def add_contenu_articles(request, sous_category_id):
    """
    Show home page.
    """
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    user = request.user
    user_avatars = UserProfile.objects.all()

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    if request.method == 'POST':

        form = addContenuArticlesForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addContenuArticlesForm()
    return render(request, "articles/add_contenu_articles.html", {"sous_category_id": sous_category_id, 
    'picture_user': picture_user, 'form': form, 'sous_categorys': sous_categorys, "categorys": categorys})

def add_title_articles(request, sous_category_id):
    """
    Show home page.
    """
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    user = request.user
    user_avatars = UserProfile.objects.all()

    for user_avatar in user_avatars:
        # print(user_avatar.user_id)
        # print(user.id)
        if user_avatar.user_id == user.id:
            picture_user = user_avatar.avatar
            # print(picture_user)
            break
    else:
        picture_user = ""

    if request.method == 'POST':

        form = addTitleArticlesForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addTitleArticlesForm()
    return render(request, "articles/add_title_articles.html", {"sous_category_id": sous_category_id, 
    'picture_user': picture_user, 'form': form, 'sous_categorys': sous_categorys, "categorys": categorys})