from rest_framework import serializers
from .models import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = "__all__"