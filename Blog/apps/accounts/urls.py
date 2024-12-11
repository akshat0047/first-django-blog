from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView
from django.contrib.auth import views as auth_views
from .forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from django.urls import path, include
from . import views as v

app_name = "accounts"

urlpatterns = [
     path('register/', v.signup, name="register"),
     path('login/', LoginView.as_view(form_class=AuthenticationForm, template_name='accounts/login.html'), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),

     path('password-change/', PasswordChangeView.as_view(template_name='accounts/password_change_form.html',
                                                            form_class=PasswordChangeForm), name='password_change'),
     path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html',), name='password_change_done'),

     path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset_form.html', form_class=PasswordResetForm,
                                                       email_template_name='accounts/password_reset_email.html'), name='password_reset'),
     path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', form_class=SetPasswordForm), name='password_reset_confirm'),
     path('reset/done/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete')
]
