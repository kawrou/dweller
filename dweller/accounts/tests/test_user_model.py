from django.db import IntegrityError
from django.test import TestCase
import pytest
from accounts.models import User as UserModel
from django.contrib.auth import get_user_model

User: type[UserModel] = get_user_model()

normal_user = {
    'email': "normal@user.com",
    'password': "foo",
    'first_name': "John",
    'last_name': "Doe",
    'dob': "1990-01-01"
}

def create_user() -> UserModel:
    return User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

# Create your tests here.
@pytest.mark.django_db
def test_create_user() -> None:
    user = create_user()

    assert user.email == normal_user["email"]
    assert user.first_name == normal_user["first_name"]
    assert user.last_name == normal_user["last_name"]
    assert user.date_of_birth == normal_user["dob"]
    assert user.check_password("foo")
    assert user.is_active 
    assert not user.is_staff 
    assert not user.is_superuser 

@pytest.mark.django_db
def test_unique_email():
    create_user()

    with pytest.raises(IntegrityError):
        create_user()

@pytest.mark.django_db
def test_hashed_password():
    user = create_user()

    assert user.password != normal_user["password"]
    assert user.check_password(normal_user["password"]) is True

@pytest.mark.django_db
def test_user_creation_fails_without_email():
    with pytest.raises(ValueError):
        User.objects.create_user(
            email="", 
            password=normal_user["password"], 
            first_name=normal_user["first_name"], 
            last_name=normal_user["last_name"], 
            date_of_birth=normal_user["dob"]
        )

@pytest.mark.django_db
def test_user_str_representation():
    user = create_user()
    assert str(user) == "normal@user.com"

@pytest.mark.django_db
def test_create_superuser():
    admin_user = User.objects.create_superuser(
        email="admin@user.com", 
        first_name="Super", 
        last_name="Admin", 
        password="foo",
        date_of_birth="1990-01-01"
    )

    assert admin_user.email == "admin@user.com"
    assert admin_user.check_password("foo")
    assert admin_user.is_active is True
    assert admin_user.is_staff is True 
    assert admin_user.is_superuser is True 
