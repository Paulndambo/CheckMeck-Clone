from rest_framework import serializers

from .models import GarageSubscription


class GarageSubscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for GarageSubscription model.
    """
    class Meta:
        model = GarageSubscription
        fields = '__all__'