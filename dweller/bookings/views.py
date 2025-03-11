from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def trips_view(request: HttpRequest):
    return render(request, 'bookings/trips.html')
