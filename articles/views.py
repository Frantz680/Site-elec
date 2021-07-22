from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import UserProfile
from home.models import Sous_Category, Category
from home.forms import Articles, addArticlesForm

# Create your views here.

def view_articles(request, sous_category):
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
    
    sous_category = Sous_Category.objects.get(name=sous_category)
    articles = Articles.objects.filter(sous_category_id=sous_category.id)
    return render(request, "articles/detail.html", {"sous_category": sous_category, 'picture_user': picture_user, "articles": articles, 'sous_categorys': sous_categorys, "categorys": categorys})

def add_articles(request, sous_category_id):
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

        form = addArticlesForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = addArticlesForm()
    return render(request, "articles/add_articles.html", {"sous_category_id": sous_category_id, 'picture_user': picture_user, 'form': form, 'sous_categorys': sous_categorys, "categorys": categorys})

