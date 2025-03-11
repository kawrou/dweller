from django.urls import path
from .views import trips_view

urlpatterns = [
    path("trips/", trips_view, name="trips"),
]
