from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
@login_required
def trips_view(request: HttpRequest):
    return render(request, 'bookings/trips.html')
