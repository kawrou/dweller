import pytest
from django.urls import reverse
from bookings.models import Booking
from tests.conftest_global import test_user1, test_user2, test_booking1, test_booking2
from accounts.models import User
from django.contrib.auth import get_user_model

UserModel: User = get_user_model()

@pytest.mark.django_db
def test_trips_view_no_bookings(client, test_user1):
    client.force_login(test_user1)
    response = client.get(reverse("trips"))

    assert response.status_code == 200
    assert len(response.context['bookings']) == 0
    assert "You currently have no trips booked" in response.content.decode()

@pytest.mark.django_db
def test_trips_view_with_bookings(client, test_user1, test_booking1):
    client.force_login(test_user1)
    response = client.get(reverse("trips"))

    assert response.status_code == 200
    assert test_booking1.destination in response.content.decode()

@pytest.mark.django_db
def test_trips_view_redirects_unauthenticated_users(client):
    response = client.get(reverse("trips"))

    assert response.status_code == 302
    assert response.url.startswith("/accounts/login/")

@pytest.mark.django_db
def test_authenticated_users_only_see_own_trips(client, test_user1, test_user2, test_booking1, test_booking2):
    client.force_login(test_user1)
    response = client.get(reverse("trips"))
    assert test_booking2.destination not in response.content.decode()
    assert test_booking1.destination in response.content.decode()

    client.force_login(test_user2)
    response = client.get(reverse("trips"))
    assert test_booking1.destination not in response.content.decode()
    assert test_booking2.destination in response.content.decode()