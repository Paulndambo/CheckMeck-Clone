from rest_framework import serializers
from .models import NotificationMessage

class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationMessage
        fields = "__all__"