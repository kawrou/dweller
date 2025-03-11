from django.urls import path
from .views import trips_view

urlpatterns = [
    path("", trips_view, name="trips"),
]
