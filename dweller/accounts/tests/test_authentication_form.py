import pytest
from accounts.models import User as UserModel
from accounts.forms import CustomAuthenticationForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, get_user_model

User: UserModel = get_user_model()

normal_user = {
    'email': "normal@user.com",
    'password': "a;lksjfa!@#!",
    'first_name': "John",
    'last_name': "Doe",
    'dob': "1990-01-01"
}
# Create your tests here.
@pytest.mark.django_db
def test_valid_form_authenticates_user():
    User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    assert authenticate(username=normal_user["email"], password=normal_user["password"]) != None

    form = CustomAuthenticationForm(
        data={
            "username": normal_user["email"], 
            "password": normal_user["password"]
        }
    )

    assert form.is_valid()
    assert not form.errors

@pytest.mark.django_db
def test_invalid_password_fails_authentication():
    form = CustomAuthenticationForm(
        data={
            "username": normal_user["email"], 
            "password": "wrongpassword"
        }
    )

    assert not form.is_valid()
    assert form.errors

@pytest.mark.django_db
def test_non_exisent_user_fails_authentication():
    form = CustomAuthenticationForm(
        data={
            "username": "non-existant-user@test.com", 
            "password": "wrongpassword123"
        }
    )

    assert not form.is_valid()
    assert form.errors

@pytest.mark.django_db
def test_inactive_user_cannot_authenticate():
    inactive_user = User.objects.create_user(
        email="inactive@test.com",
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"],
        is_active=False
    )

    form = CustomAuthenticationForm(
        data={
            "username": "inactive@test.com", 
            "password": "strongpassword123"
        }
    )

    assert not form.is_valid()
    assert form.errors
