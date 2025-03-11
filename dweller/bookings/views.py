from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest
from bookings.models import Booking

# Create your views here.
@login_required
def trips_view(request: HttpRequest):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/trips.html', {"bookings": user_bookings})
