from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home.views import home, add, add_cat, \
    add_picture_carrousel, ml, add_actu, all_actu

urlpatterns = [
    path('', home, name='home'),
    path('mentions-legals', ml, name='ml'),
    path('add_sous_cat/<slug:id_cat>/', add, name='add'),
    path('add_cat/', add_cat, name='add_cat'),
    path('add_picture/', add_picture_carrousel, name='add_picture_carrousel'),
    path('add_actualites/', add_actu, name='add_actu'),
    path('actualite/', all_actu, name='all_actu'),
    path('articles/', include('articles.urls')),
    # path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
