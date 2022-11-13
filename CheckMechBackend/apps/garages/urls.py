from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("garage-subscriptions", views.GarageSubscriptionModelViewSet, basename="garage-subscriptions")

urlpatterns = [
    path("", include(router.urls)),
]