import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import User as UserModel

User: UserModel = get_user_model()

def create_user_in_db(normal_user) -> UserModel:
    return User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

@pytest.mark.django_db
def test_logout_redirect(client, normal_user):
    create_user_in_db(normal_user)

    response = client.post(reverse("logout"),)

    assert response.status_code == 302
    assert response.url == reverse("login")
    
@pytest.mark.django_db
def test_logout_clears_session(client, normal_user):
    create_user_in_db(normal_user)

    client.login(username=normal_user["email"], password=normal_user["password"])
    assert client.session.keys() 

    client.post(reverse("logout"),)
    assert not client.session.keys() 

@pytest.mark.django_db
def test_logsout_when_user_not_logged_in(client):
    response = client.post(reverse("logout"),)

    assert response.status_code == 302
    assert response.url == reverse("login")
