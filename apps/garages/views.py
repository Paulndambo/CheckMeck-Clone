from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .distance_calculator import calculate_distance
from .filters import GarageFilter
from django.db.models import Q


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
        
    
class GarageListAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = Garage.objects.all()
    serializer_class = GarageListSerializer
    http_method_names = ['get']

    #filter_backends = [DjangoFilterBackend, SearchFilter]
    #filterset_class = GarageFilter
    #filterset_fields = ["town"]
    #search_fields = ["town"]

    def get(self, request):
        garages = Garage.objects.all()
        #print(f"Name: {self.request.GET.get["lat"]}")
        serializer = self.serializer_class(instance=garages, many=True)


        town = self.request.GET.get('town')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if town:
            garages_list = Garage.objects.filter(Q(town__icontains=town))
            serializer = self.serializer_class(instance=garages_list, many=True)

        if latitude and longitude:
            print(f"Lat: {latitude}, Long: {longitude}")
            garages_found = []
            try:
                for garage in garages:
                    distance = calculate_distance(
                    garage_location={
                        "latitude": garage.location['latitude'],
                        "longitude": garage.location['longitude']
                    },
                    driver_location={
                        "latitude": latitude,
                        "longitude": longitude
                    }
                )
                if distance <= 10:
                    garages_found.append(garage)
            
            except Exception as e:
                raise
            print(garages_found)
            serializer = self.serializer_class(instance=garages_found, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_200_OK)

    

