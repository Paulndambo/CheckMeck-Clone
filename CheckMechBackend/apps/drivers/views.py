from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CarSerializer, DriverSerializer, CarListSerializer
from .models import Car, Driver
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.
class DriverModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Driver.objects.all()
        return Driver.objects.filter(user=user)

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}


class CarModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id,
            'driver_id': self.kwargs['driver_pk']
            }

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Car.objects.all()
        return Car.objects.filter(driver__user=user)


class CarListModelViewSet(ModelViewSet):
    #permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarListSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['number_plate', 'brand', 'car_model',
                        'driver__first_name', 'driver__last_name', 'year_manufactured']
    search_fields = ["number_plate", "driver__user__email", "driver__phone_number", 'brand', 'car_model', 'year_manufactured']
