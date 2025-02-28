from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import User as UserModel

User: type[UserModel] = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "first_name", "last_name", "date_of_birth", "password1", "password2"]

    def save(self, commit = True) -> UserModel:
        user: UserModel = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
