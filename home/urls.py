from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home.views import home, add, add_cat

urlpatterns = [
    path('', home, name='home'),
    path('add_sous_cat/<slug:id_cat>/', add, name='add'),
    path('add_cat/', add_cat, name='add_cat'),
    path('lumiere/', include('lumiere.urls')),
    path('prise/', include('prise_elec.urls')),
    path('tableau/', include('tableau.urls')),
    path('articles/', include('articles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)