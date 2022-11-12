from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("car-brands", views.CarBrandModelViewSet, basename="car-brands")

urlpatterns = [
    path("", include(router.urls)),
]