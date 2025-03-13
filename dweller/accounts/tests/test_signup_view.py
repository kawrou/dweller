import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_signup_page_loads(client):
    response = client.get(reverse("signup"))
    assert response.status_code == 200 

@pytest.mark.django_db
def test_signup_view_uses_correct_template(client):
    response = client.get(reverse("signup"))
    assert "accounts/signup.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_valid_signup_redirect(client, valid_form_data):
    response = client.post(reverse("signup"), valid_form_data)
    assert response.status_code == 302
    assert response.url == reverse("home")

@pytest.mark.django_db
def test_unmatched_passwords_shows_errors(client, invalid_password_not_matched_form_data):
    response = client.post(reverse("signup"), invalid_password_not_matched_form_data)
    assert response.status_code == 200
    assert "form" in response.context
    
    form = response.context["form"]
    assert not form.is_valid()
    assert "password2" in form.errors

@pytest.mark.django_db
def test_missing_first_name_shows_error(client, invalid_missing_first_name_form_data):
    response = client.post(reverse("signup"), invalid_missing_first_name_form_data)
    assert response.status_code == 200
    assert "form" in response.context
    
    form = response.context["form"]
    assert not form.is_valid()
    assert "first_name" in form.errors

@pytest.mark.django_db
def test_missing_last_name_shows_error(client, invalid_missing_last_name_form_data):
    response = client.post(reverse("signup"), invalid_missing_last_name_form_data)
    assert response.status_code == 200
    assert "form" in response.context
    
    form = response.context["form"]
    assert not form.is_valid()
    assert "last_name" in form.errors
