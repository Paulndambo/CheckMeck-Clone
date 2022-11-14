from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
#router.register("garage-subscriptions", views.GarageSubscriptionModelViewSet, basename="garage-subscriptions")

router.register('garage-subscriptions', views.GarageSubscriptionViewSet, basename='garage-subscriptions')
router.register('', views.GarageViewSet, basename='garages')
router.register('services', views.ServiceViewSet, basename='services')
urlpatterns = [
    path("", include(router.urls)),
]