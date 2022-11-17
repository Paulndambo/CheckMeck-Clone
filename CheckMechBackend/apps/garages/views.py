from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import GarageSubscription, Garage, Service, GarageOwner
from .serializers import GarageSubscriptionSerializer, GarageSerializer, ServiceSerializer, GarageOwnerSerializer, GarageListSerializer

class GarageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    

    def get_queryset(self):
        user = self.request.user
        owner = GarageOwner.objects.get(user=user)
        if user.is_staff:
            return Garage.objects.all()
        return Garage.objects.filter(owner=owner)
    

class GarageSubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GarageSubscription.objects.all()
    serializer_class = GarageSubscriptionSerializer
    

    def get_queryset(self):
        return GarageSubscription.objects.filter(garage_id=self.kwargs['garage_pk'])


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(garage_id=self.kwargs['garage_pk'])


class GarageOwnerModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GarageOwner.objects.all()
    serializer_class = GarageOwnerSerializer

    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return GarageOwner.objects.all()
        return GarageOwner.objects.filter(user=user)
        
    
class GarageListModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Garage.objects.all()
    serializer_class = GarageListSerializer
    http_method_names = ['get']

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name", "town"]
    search_fields = ["name", "town"]

