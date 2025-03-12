import pytest
from django.urls import reverse
from bookings.models import Booking
from tests.conftest_global import normal_user
from accounts.models import User
from django.contrib.auth import get_user_model

UserModel: User = get_user_model()

@pytest.mark.django_db
def test_trips_view_no_bookings(client, normal_user):
    user = User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    client.force_login(user)
    response = client.get(reverse("trips"))

    assert response.status_code == 200
    assert "You currently have no trips booked" in response.content.decode()

@pytest.mark.django_db
def test_trips_view_with_bookings(client, normal_user):
    user = User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    booking = Booking.objects.create(
        user=user,
        destination="Paris"
    )

    client.force_login(user)

    response = client.get(reverse("trips"))

    assert response.status_code == 200
    assert booking.destination in response.content.decode()

@pytest.mark.django_db
def test_trips_view_redirects_unauthenticated_users(client):
    response = client.get(reverse("trips"))

    assert response.status_code == 302
    assert response.url.startswith("/accounts/login/")
