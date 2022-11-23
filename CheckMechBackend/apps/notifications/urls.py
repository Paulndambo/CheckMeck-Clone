from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.SendSMSAPIView.as_view(), name="send-sms"),
]