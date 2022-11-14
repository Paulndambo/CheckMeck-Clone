from rest_framework import serializers

from .models import GarageSubscription, Garage, Service

class GarageSubscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for GarageSubscription model.
    """
    class Meta:
        model = GarageSubscription
        fields = '__all__'

class GarageSerializer(serializers.ModelSerializer):
    """
    Serializer for Garage model.
    """
    class Meta:
        model = Garage
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Service model.
    """
    class Meta:
        model = Service
        fields = '__all__'

