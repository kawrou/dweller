from django.test import TestCase
import pytest
from tests.conftest_global import test_user1, test_user2 
from bookings.models import Booking

def create_paris_booking(user):
    return Booking.objects.create(
        user = user,
        destination="Paris"
    )

def create_italy_booking(user):
    return Booking.objects.create(
        user = user,
        destination="Italy"
    )

# Create your tests here.
@pytest.mark.django_db
def test_create_booking(test_user1):
    booking = create_paris_booking(test_user1)

    assert Booking.objects.count() == 1
    assert booking.user == test_user1
    assert booking.destination == "Paris"
    assert str(booking) == "Booking by user1@user.com to Paris"

@pytest.mark.django_db
def test_booking_query_for_single_user(test_user1):
    booking1 = create_paris_booking(test_user1)
    booking2 = create_italy_booking(test_user1)

    bookings = Booking.objects.filter(user=test_user1)

    assert bookings.count() == 2
    assert booking1 in bookings and booking2 in bookings

@pytest.mark.django_db
def test_booking_query_for_multiple_user(test_user1, test_user2):
    booking1 = create_paris_booking(test_user1)
    booking2 = create_italy_booking(test_user2)

    user1_booking = Booking.objects.filter(user=test_user1)
    user2_booking = Booking.objects.filter(user=test_user2)

    assert user1_booking.count() == 1
    assert booking1 in user1_booking
    assert booking2 not in user1_booking

    assert user2_booking.count() == 1
    assert booking2 in user2_booking
    assert booking1 not in user2_booking

@pytest.mark.django_db
def test_user_deletion_cascase(test_user1):
    booking = create_paris_booking(test_user1)
    assert Booking.objects.count() == 1

    test_user1.delete()
    assert Booking.objects.count() == 0