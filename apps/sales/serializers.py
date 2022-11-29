from rest_framework import serializers
from apps.garages.models import Garage

class GarageOnboardingSerializer(serializers.Serializer):
    owner = serializers.JSONField()
    garage_details = serializers.JSONField()
    services = serializers.JSONField()
    
