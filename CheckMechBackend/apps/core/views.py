from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarBrandSerializer
from .models import CarBrand
# Create your views here.
class CarBrandModelViewSet(ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer