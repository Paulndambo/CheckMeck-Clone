from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import GarageSubscription, Garage, Service
from .serializers import GarageSubscriptionSerializer, GarageSerializer, ServiceSerializer


# Create your views here.
# class GarageSubscriptionModelViewSet(ModelViewSet):
#     queryset = GarageSubscription.objects.all()
#     serializer_class = GarageSubscriptionSerializer
    #permission_classes = (IsAuthenticated,)


# class GarageSubscriptionAPIView(generics.ListCreateAPIView):
#     queryset = GarageSubscription.objects.all()
#     serializer_class = GarageSubscriptionSerializer

#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def get(self, request):
#         user = request.user
#         subscriptions = GarageSubscription.objects.filter(garage__user=user)
#         serializer = self.serializer_class(subscriptions, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class GarageSubscriptionRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDeleteAPIView):
#     queryset = GarageSubscription.objects.all()
#     serializer_class = GarageSubscriptionSerializer

#     lookup_field = "pk"

class GarageSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = GarageSubscription.objects.all()
    serializer_class = GarageSubscriptionSerializer
    #permission_classes = (IsAuthenticated)

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    #permission_classes = (IsAuthenticated,)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

