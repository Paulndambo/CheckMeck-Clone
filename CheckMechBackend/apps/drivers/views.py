from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CarSerializer, DriverSerializer
from .models import Car, Driver
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