from django.db import IntegrityError
from django.test import TestCase
import pytest
from accounts.models import User as UserModel
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

#User: type[UserModel] = get_user_model()

valid_form_data = {
    'email': "normal@user.com",
    'first_name': "John",
    'last_name': "Doe",
    'date_of_birth': "1990-01-01",
    'password1': "StrongPassword123!",
    'password2': "StrongPassword123!",
}

invalid_form_data = {
    'email': "normal@user.com",
    'first_name': "John",
    'last_name': "Doe",
    'date_of_birth': "1990-01-01",
    'password1': "StrongPassword123!",
    'password2': "StrongPassword123!",
}

#def create_user() -> UserModel:
#    return User.objects.create_user(
#        email=valid_form_data["email"], 
#        password=valid_form_data["password"], 
#        first_name=valid_form_data["first_name"],
#        last_name=valid_form_data["last_name"],
#        date_of_birth=valid_form_data["dob"]
#    )

# Create your tests here.
@pytest.mark.django_db
def test_create_user() -> None:
    form = CustomUserCreationForm(data=valid_form_data)

    assert form.is_valid() == True
    assert not form.errors

    user = form.save()
    assert user.email== valid_form_data["email"]
    assert user.check_password(valid_form_data["password1"])

@pytest.mark.django_db
def test_hashed_password() -> None:
    form = CustomUserCreationForm(data=valid_form_data)

    user = form.save()
    assert user.password != valid_form_data["password1"]
