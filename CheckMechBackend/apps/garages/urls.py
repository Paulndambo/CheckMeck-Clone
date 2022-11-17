from django.urls import include, path
#from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
#router.register("garage-subscriptions", views.GarageSubscriptionModelViewSet, basename="garage-subscriptions")
router.register("garages-list", views.GarageListModelViewSet, basename="garages-list")
router.register("garage-owners", views.GarageOwnerModelViewSet,basename="garage-owners")
router.register('garages', views.GarageViewSet, basename='garages')
garage_routers = routers.NestedDefaultRouter(router, "garages", lookup="garage")
garage_routers.register('garage-subscriptions',
                        views.GarageSubscriptionViewSet, basename='garage-subscriptions')
garage_routers.register('services', views.ServiceViewSet, basename='services')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(garage_routers.urls)),
]