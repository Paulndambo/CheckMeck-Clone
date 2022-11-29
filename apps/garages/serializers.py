from rest_framework import serializers
from .models import GarageSubscription, Garage, Service, GarageOwner

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

class GarageOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarageOwner
        fields = "__all__"


class GarageListSerializer(serializers.ModelSerializer):
    subscriptions = serializers.SerializerMethodField(read_only=True)
    services = serializers.SerializerMethodField(read_only=True)
    owner_details = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Garage
        fields = ["id", "name", "logo", "phone_number", "dealership_affiliations", 
        "location", "postal_address", "town", "country", "subscription", "subscription_status", 
        "services", "subscriptions", "owner_details", "created", "modified"]

    
    def get_services(self, obj):
        return obj.services.values()

    def get_subscriptions(self, obj):
        return obj.subscriptions.values()

    def get_owner_details(self, obj):
        return GarageOwner.objects.filter(id=obj.owner.id).values()