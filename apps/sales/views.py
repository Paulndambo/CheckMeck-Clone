from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import GarageOnboardingSerializer
from .mixins import GarageOnboardingMixin
from django.contrib.auth.models import User
# Create your views here.


class GarageOnboardingAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = GarageOnboardingSerializer

    def post(self, request):
        data = request.data
        email = data['owner']['email']
        user = User.objects.filter(email=email).first()
        if user:
            return Response({"failed": "User with this email exists already"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            try:
                onbording_mixin = GarageOnboardingMixin(data=data)
                onbording_mixin.run()
            except Exception as e:
                raise e
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
