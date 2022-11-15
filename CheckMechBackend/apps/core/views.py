from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarBrandSerializer, ProfilePhotoSerializer
from .models import CarBrand, ProfilePhoto
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CarBrandModelViewSet(ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class ProfilePhotoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProfilePhoto.objects.all()
    serializer_class = ProfilePhotoSerializer

    def get_queryset(self):
        user = self.request.user
        return ProfilePhoto.objects.filter(user=user)