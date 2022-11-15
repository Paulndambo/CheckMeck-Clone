from rest_framework import serializers
from .models import GarageSubscription, Garage, Service

class GarageSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarageSubscription
        fields = '__all__'


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

