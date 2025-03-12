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

@pytest.mark.django_db
def test_authenticated_users_only_see_own_trips(client, normal_user):
    user1 = User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

    user2 = User.objects.create_user(
        email="user2@user.com",
        password="bar",
        first_name="John",
        last_name="Doe",
        date_of_birth="1987-01-01"
    )

    booking1 = Booking.objects.create(
        user=user1,
        destination="Paris"
    )

    booking2 = Booking.objects.create(
        user=user2,
        destination="London"
    )

    client.force_login(user1)
    response = client.get(reverse("trips"))
    assert booking2.destination not in response.content.decode()

    client.force_login(user2)
    response = client.get(reverse("trips"))
    assert booking1.destination not in response.content.decode()
