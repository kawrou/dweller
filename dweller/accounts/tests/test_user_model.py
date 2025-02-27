from django.db import IntegrityError
from django.test import TestCase
import pytest
from accounts.models import User

# Create your tests here.
@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email="normal@user.com", password="foo")

    assert user.email == "normal@user.com"
    assert user.check_password("foo")
    assert user.is_active 
    assert not user.is_staff 
    assert not user.is_superuser 

@pytest.mark.django_db
def test_unique_email():
    User.objects.create_user(email="unique@user.com", password="foo")

    with pytest.raises(IntegrityError):
        User.objects.create_user(email="unique@user.com", password="foo")

@pytest.mark.django_db
def test_user_str_representation():
    user = User.objects.create_user(email="normal@user.com", password="foo")
    assert str(user) == "normal@user.com"

@pytest.mark.django_db
def test_create_superuser():
    admin_user = User.objects.create_user(email="admin@user.com", password="foo")

    assert admin_user.email == "admin@user.com"
    assert admin_user.check_password("foo")
    assert admin_user.is_active 
    assert admin_user.is_staff 
    assert admin_user.is_superuser 
