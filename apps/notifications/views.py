from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import NotificationMessage
from .serializers import SmsSerializer
from .send_sms import send_notification, request_service

# Create your views here.
class SendSMSAPIView(generics.GenericAPIView):
    queryset = NotificationMessage.objects.all()
    serializer_class = SmsSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.validated_data['destination_address']
            driver_name = serializer.validated_data['driver_name']
            garage_name = serializer.validated_data['garage_name']
            content = serializer.validated_data['content']
            driver_phone_number = serializer.validated_data['driver_phone_number']
            try:
                #send_notification(phone_number, content, 'SMS')
                request_service(garage_name, phone_number, driver_name, driver_phone_number)
            except Exception as e:
                raise e
            print(phone_number)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        messages = NotificationMessage.objects.all()
        serializer = self.serializer_class(instance=messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)