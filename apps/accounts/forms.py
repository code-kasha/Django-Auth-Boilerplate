from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import User


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")
