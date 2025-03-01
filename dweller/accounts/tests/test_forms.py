from django.db import IntegrityError
from django.test import TestCase
import pytest
from accounts.models import User as UserModel
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from datetime import date, timedelta

User: UserModel = get_user_model()

valid_form_data = {
    'email': "normal@user.com",
    'first_name': "John",
    'last_name': "Doe",
    'date_of_birth': "1990-01-01",
    'password1': "StrongPassword123!",
    'password2': "StrongPassword123!",
}

invalid_password_not_matched_form_data = {
    'email': "normal@user.com",
    'first_name': "John",
    'last_name': "Doe",
    'date_of_birth': "1990-01-01",
    'password1': "StrongPassword123!",
    'password2': "StrongPassword456!",
}

invalid_password_too_short_form_data = {
    'email': "normal@user.com",
    'first_name': "John",
    'last_name': "Doe",
    'date_of_birth': "1990-01-01",
    'password1': "foo",
    'password2': "foo",
}

invalid_user_not_18_form_data = {
    'email': "normal@user.com",
    'first_name': "John",
    'last_name': "Doe",
    'date_of_birth': date.today() - timedelta(days=365 * 17), 
    'password1': "StrongPassword123!",
    'password2': "StrongPassword123!",
}

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

@pytest.mark.django_db
def test_password_field_must_match() -> None:
    """Test that passwords must match"""
    form = CustomUserCreationForm(data=invalid_password_not_matched_form_data)

    assert form.is_valid() == False
    assert form.errors is not None and "password2" in dict(form.errors)

@pytest.mark.django_db
def test_password_field_too_short() -> None:
    form = CustomUserCreationForm(data=invalid_password_too_short_form_data)

    assert form.is_valid() == False
    assert form.errors is not None and "password2" in form.errors


@pytest.mark.django_db
def test_email_must_be_unique() -> None:
    User.objects.create_user(
        email=valid_form_data["email"], 
        password=valid_form_data["password1"], 
        first_name=valid_form_data["first_name"],
        last_name=valid_form_data["last_name"],
        date_of_birth=valid_form_data["date_of_birth"]
    )

    form = CustomUserCreationForm(data=valid_form_data)

    assert form.is_valid() == False
    assert form.errors is not None and "email" in form.errors

@pytest.mark.django_db
def test_user_must_be_at_least_18() -> None:
    form = CustomUserCreationForm(data=invalid_user_not_18_form_data)

    assert form.is_valid() == False
    assert form.errors is not None and "date_of_birth" in form.errors
