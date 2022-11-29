from django.urls import path, include
from .import views

urlpatterns = [
    path("request-service/", views.SendSMSAPIView.as_view(), name="request-service"),
]