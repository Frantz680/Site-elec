from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home.views import home

urlpatterns = [
    path('', home, name='home'),
    path('lumiere/', include('lumiere.urls')),
    path('prise/', include('prise_elec.urls')),
    path('tableau/', include('tableau.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)