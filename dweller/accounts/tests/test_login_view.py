import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import User

UserModel: User = get_user_model()

@pytest.mark.django_db
def test_login_page_loads(client):
    response = client.get(reverse("login"))
    assert response.status_code == 200 

@pytest.mark.django_db
def test_login_view_uses_correct_template(client):
    response = client.get(reverse("login"))
    assert "accounts/login.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_valid_login_redirect(client, normal_user):
    User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    response = client.post(
        reverse("login"), 
        {"username":normal_user["email"], "password":normal_user["password"]}
    )

    assert response.status_code == 302
    assert response.url == reverse("trips")

@pytest.mark.django_db
def test_unmatched_passwords_shows_errors(client, normal_user):
    User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    response = client.post(
        reverse("login"),
        {"username":normal_user["email"], "password":"WrongPassword123"}
    )

    assert response.status_code == 200
    assert "form" in response.context
    
    form = response.context["form"]
    assert not form.is_valid()
    assert "__all__" in form.errors

@pytest.mark.django_db
def test_unmatched_email_shows_errors(client, normal_user):
    User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    response = client.post(
        reverse("login"),
        {"username":"wrong_email@test.com", "password":normal_user["password"]}
    )

    assert response.status_code == 200
    assert "form" in response.context
    
    form = response.context["form"]
    assert not form.is_valid()
    assert "__all__" in form.errors
