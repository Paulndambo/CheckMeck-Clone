from rest_framework import serializers
from .models import Driver, Car
from django.contrib.auth.models import User
from django.db import transaction

class DriverSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Driver
        fields = ["id", "first_name", "last_name", 
                    "phone_number", "license_number", 
                    "id_number", "kra_pin", "birth_date", "gender", 
                    "marital_status", "postal_code", "town", "country", "user"]

    def create(self, validated_data):
        user_id = self.context['user_id']
        user=User.objects.get(id=user_id)
        return Driver.objects.create(user=user, **validated_data)

    def get_user(self, obj):
        return obj.user.id


class CarSerializer(serializers.ModelSerializer):
    #driver = DriverSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ["id", "number_plate", "car_color", "brand", "car_model", "year_manufactured", "engine_capacity"]
    
    #@transaction.atomic
    def create(self, validated_data):
        driver_id = self.context['driver_id']
        driver = Driver.objects.get(id=driver_id)
        return Car.objects.create(driver=driver, **validated_data)


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
