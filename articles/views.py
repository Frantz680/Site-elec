from django.shortcuts import render, redirect
from django.contrib import messages

from home.models import Sous_Category
from home.forms import Articles

# Create your views here.

def view_articles(request, sous_category):
    """
    Show home page.
    """
    
    sous_category = Sous_Category.objects.get(name=sous_category)
    articles = Articles.objects.filter(sous_category_id=sous_category.id)
    return render(request, "articles/detail.html", {"sous_category": sous_category, "articles": articles})

# def add_tool(request, sous_category_id):
#     """
#     Show home page.
#     """
#     if request.method == 'POST':

#         form_tool = addToolForm(request.POST, request.FILES)
#         print(form_tool)

#         if form_tool.is_valid():
            
#             form_tool.save()
#             messages.success(request, 'Votre compte a été crée avec succès.')
#             return redirect('home')
#     else:
#         form_tool = addToolForm()
#     return render(request, "tools/add_tool.html", {"sous_category_id": sous_category_id, 'form_tool': form_tool})

