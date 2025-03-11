from django.test import TestCase
import pytest
from accounts.models import User as UserModel
from django.contrib.auth import get_user_model
from tests.conftest_global import normal_user

from bookings.models import Booking

User: UserModel = get_user_model()

def create_user(normal_user) -> UserModel:
    return User.objects.create_user(
        email=normal_user["email"], 
        password=normal_user["password"], 
        first_name=normal_user["first_name"],
        last_name=normal_user["last_name"],
        date_of_birth=normal_user["dob"]
    )

# Create your tests here.
@pytest.mark.django_db
def test_create_booking(normal_user):
    user = create_user(normal_user)

    booking = Booking.objects.create(
        user = user,
        destination="Paris"
    )

    assert Booking.objects.count() == 1
    assert booking.user == user
    assert booking.destination == "Paris"
    assert str(booking) == "Booking by normal@user.com to Paris"

@pytest.mark.django_db
def test_booking_query(normal_user):
    user = create_user(normal_user)
    booking1 = Booking.objects.create(
        user = user,
        destination = "Paris"
    )
    booking2 = Booking.objects.create(
        user = user,
        destination = "Italy"
    )

    bookings = Booking.objects.filter(user=user)

    assert bookings.count() == 2
    assert booking1, booking2 in bookings

@pytest.mark.django_db
def test_user_deletion_cascase(normal_user):
    user = create_user(normal_user)

    booking = Booking.objects.create(
        user = user,
        destination="Paris"
    )

    assert Booking.objects.count() == 1

    user.delete()

    assert Booking.objects.count() == 0

