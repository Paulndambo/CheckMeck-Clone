from django.urls import path
from .import views

urlpatterns = [
    path("garage-onboarding/", views.GarageOnboardingAPIView.as_view(), name="garage-onboarding"),
]