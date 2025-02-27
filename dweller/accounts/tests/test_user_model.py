from django.db import IntegrityError
from django.test import TestCase
import pytest
from accounts.models import User
from django.conf import settings

normal_user = {
    'email': "normal@user.com",
    'password': "foo",
    'first_name': "John",
    'last_name': "Doe",
    'dob': "1990-01-01"
}

def create_user() -> User:
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

    assert user.email == "normal@user.com"
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
    assert admin_user.is_active 
    assert admin_user.is_staff 
    assert admin_user.is_superuser 
