from django.db import IntegrityError
from django.test import TestCase
import pytest
# from tests.conftest_global import test_user1
from accounts.models import User as UserModel
from django.contrib.auth import get_user_model

CustomerUser = get_user_model()

def create_user(normal_user) -> UserModel:
    return CustomerUser.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

# Create your tests here.
@pytest.mark.django_db
def test_create_user(normal_user) -> None:
    user = create_user(normal_user)

    assert user.email == normal_user["email"]
    assert user.first_name == normal_user["first_name"]
    assert user.last_name == normal_user["last_name"]
    assert user.date_of_birth == normal_user["dob"]
    assert user.check_password(normal_user["password"])
    assert user.is_active 
    assert not user.is_staff 
    assert not user.is_superuser 

@pytest.mark.django_db
def test_unique_email(normal_user):
    create_user(normal_user)

    with pytest.raises(IntegrityError):
        create_user(normal_user)

@pytest.mark.django_db
def test_hashed_password(normal_user):
    user = create_user(normal_user)

    assert user.password != normal_user["password"]
    assert user.check_password(normal_user["password"]) is True

@pytest.mark.django_db
def test_user_creation_fails_without_email(normal_user):
    with pytest.raises(ValueError):
        CustomerUser.objects.create_user(
            email="", 
            password=normal_user["password"], 
            first_name=normal_user["first_name"], 
            last_name=normal_user["last_name"], 
            date_of_birth=normal_user["dob"]
        )

@pytest.mark.django_db
def test_user_str_representation(normal_user):
    user = create_user(normal_user)
    assert str(user) == "user1@user.com"

@pytest.mark.django_db
def test_create_superuser():
    admin_user = CustomerUser.objects.create_superuser(
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
