from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy

from django_registration.backends.activation.views import RegistrationView, ActivationView

from django.views.generic import TemplateView

from apps.accounts.forms import UserForm


class Login(LoginView):
    template_name = "accounts/login.html"
    redirect_url = reverse_lazy("home")


class Logout(LogoutView):
    pass


class ChangePassword(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("home")


class ResetPassword(PasswordResetView):
    template_name = "accounts/reset_password.html"


class ResetPasswordDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"


class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


class Register(RegistrationView):
    form_class = UserForm


class ActivateUser(ActivationView):
    pass


class RegisterComplete(TemplateView):
    template_name = "django_registration/registration_complete.html"


class RegisterClosed(TemplateView):
    template_name = "django_registration/registration_closed.html"


class ActivationComplete(TemplateView):
    template_name = "django_registration/activation_complete.html"


class UserHome(TemplateView):
    template_name = "home.html"
