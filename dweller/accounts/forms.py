from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import User as UserModel
import datetime
from django.utils.translation import gettext as _

User: type[UserModel] = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "first_name", "last_name", "date_of_birth", "password1", "password2"]

    def clean_date_of_birth(self):
        dob = self.cleaned_data["date_of_birth"]

        today = datetime.date.today() 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValidationError(
                _("You must be at least 18 years old to register."),
            )

        return dob

    def save(self, commit = True) -> UserModel:
        user: UserModel = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
