from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


from .models import GarageSubscription, Garage, Service
from .serializers import GarageSubscriptionSerializer, GarageSerializer, ServiceSerializer

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Garage.objects.all()
        return Garage.objects.filter(user=user)


class GarageSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = GarageSubscription.objects.all()
    serializer_class = GarageSubscriptionSerializer
    #permission_classes = (IsAuthenticated)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


