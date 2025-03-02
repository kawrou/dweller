from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import User as UserModel
import datetime
from django.utils.translation import gettext as _

User: type[UserModel] = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "first_name", "last_name", "date_of_birth", "password1", "password2"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not first_name:
            raise forms.ValidationError(_("First name is required."))
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not last_name:
            raise forms.ValidationError(_("Last name is required."))
        return last_name

    def clean_date_of_birth(self):
        dob = self.cleaned_data["date_of_birth"]

        today = datetime.date.today() 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise forms.ValidationError(
                _("You must be at least 18 years old to register."),
            )

        return dob

    def save(self, commit = True) -> UserModel:
        user: UserModel = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
