from django.urls import path

from . import views

urlpatterns = [
    path("", views.FlightsView.as_view()),
    path("<int:pk>/", views.FlightDetailView.as_view(), name="flight"),
]
