import pytest
from django.contrib.auth import get_user_model
from bookings.models import Booking

CustomUser = get_user_model()

@pytest.fixture
def test_user1():
    return CustomUser.objects.create_user(
        email="user1@user.com",
        password="StrongPassword123",
        first_name="John",
        last_name="Doe",
        date_of_birth="1990-01-01",
    )

@pytest.fixture
def test_user2():
    return CustomUser.objects.create_user(
        email="user2@user.com",
        password="StrongPassword456",
        first_name="John",
        last_name="Smith",
        date_of_birth="1990-01-01",
    )

@pytest.fixture
def test_booking1(test_user1):
    return Booking.objects.create(
        user=test_user1,
        destination="Paris"
    )

@pytest.fixture
def test_booking2(test_user2):
    return Booking.objects.create(
        user=test_user2,
        destination="London"
    )