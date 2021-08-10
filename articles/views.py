from django.shortcuts import render, redirect
# from django.contrib import messages

# from accounts.models import UserProfile

from home.models import Sous_Category, Category
from home.forms import addNoteArticleForm
from home.views import request_user_avatar

from articles.models import Contenu, Title, Comment
from articles.forms import addContenuArticlesForm,\
    addTitleArticlesForm, addCommentForm


def view_articles(request, sous_category):
    """
    Display the different articles page.
    """

    picture_user = request_user_avatar(request)

    comments = Comment.objects.all()
    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    sous_category = Sous_Category.objects.get(name=sous_category)
    title_articles = \
        Title.objects.filter(sous_category_id=sous_category.id)
    contenu_articles = \
        Contenu.objects.filter(sous_category_id=sous_category.id)

    if request.method == 'POST':

        form_note = addNoteArticleForm(request.POST)

        if form_note.is_valid():

            form_note.save()
            # messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')

    else:
        form_note = addNoteArticleForm()

    if request.method == 'POST':

        form = addCommentForm(request.POST)

        if form.is_valid():

            form.save()
            # messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addCommentForm()

    return render(request, "articles/detail.html",
                  {
                    "sous_category": sous_category,
                    'picture_user': picture_user,
                    "title_articles": title_articles,
                    "contenu_articles": contenu_articles,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys,
                    "form": form,
                    "comments": comments,
                    "form_note": form_note
                  })


def add_contenu_articles(request, sous_category_id):
    """
    Add the content of an article.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':

        form = addContenuArticlesForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            # messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addContenuArticlesForm()

    return render(request, "articles/add_contenu_articles.html",
                  {
                    "sous_category_id": sous_category_id,
                    'picture_user': picture_user,
                    'form': form,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys
                  })


def add_title_articles(request, sous_category_id):
    """
    Add the title of an article.
    """

    categorys = Category.objects.all()
    sous_categorys = Sous_Category.objects.all()

    picture_user = request_user_avatar(request)

    if request.method == 'POST':

        form = addTitleArticlesForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            # messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addTitleArticlesForm()

    return render(request, "articles/add_title_articles.html",
                  {
                    "sous_category_id": sous_category_id,
                    'picture_user': picture_user,
                    'form': form,
                    'sous_categorys': sous_categorys,
                    "categorys": categorys
                  })
