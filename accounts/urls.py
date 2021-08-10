from django.urls import path, reverse_lazy
# from django.conf.urls.static import static
# from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth.views import PasswordChangeDoneView,\
    PasswordChangeView, PasswordResetCompleteView, \
    PasswordResetConfirmView, PasswordResetView, \
    PasswordResetDoneView

from .forms import LoginForm
from accounts.views import registrer_views, my_account_views

urlpatterns = [
    path('login/', views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
        authentication_form=LoginForm), name="login"),

    path('logout/', views.LogoutView.as_view(
        template_name='registration/logout.html',
        next_page='login'), name="logout"),

    path('my_account/', my_account_views, name='my_account'),

    path('register/', registrer_views, name='register'),

    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', PasswordChangeView.as_view(
        template_name='registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')),
        name='password_reset_confirm'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'),
        name='password_reset'),

    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
]
