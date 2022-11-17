from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .import views

router = routers.DefaultRouter()
router.register("drivers", views.DriverModelViewSet, basename="drivers")

drivers_router = routers.NestedDefaultRouter(router, "drivers", lookup="driver")
drivers_router.register("cars", views.CarModelViewSet, basename="cars")
router.register("cars-list", views.CarListModelViewSet, basename="cars-list")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(drivers_router.urls)),
]