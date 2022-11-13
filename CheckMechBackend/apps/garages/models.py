from apps.core.models import AbstractBaseModel
from django.conf import settings
from django.db import models

# Create your models here.
SERVICE_PROVIDER_TYPES = (
    ("garage", "Garage"),
    ("dealership", "Dealership"),
)

PRICING_TYPES = (
    ("negotiable", "Negotiable"),
    ("not_negotiable", "Not Negotiable"),
)

SUBSCRIPTION_STATUS_CHOICES = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)

SUBSCRIPTION_TYPES = (
    ("paid", "Paid"),
    ("freemium", "Freemium"),
)

PAYMENT_METHODS = (
    ("mpesa", "Mpesa"),
    ("cash", "Cash"),
    ("card", "Card"),
)


class Garage(AbstractBaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    dealership_affiliations = models.JSONField(null=True, blank=True)
    location = models.JSONField(null=True, blank=True)
    postal_address = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    subscription = models.CharField(max_length=255, choices=SUBSCRIPTION_TYPES, default='freemium')
    subscription_status = models.CharField(max_length=255, choices=SUBSCRIPTION_STATUS_CHOICES, default="active")


    def __str__(self):
        return self.name


class Service(AbstractBaseModel):
    provider = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    pricing_type = models.CharField(max_length=255, choices=PRICING_TYPES)

    def __str__(self):
        return self.name


class GarageSubscription(AbstractBaseModel):
    garage = models.ForeignKey(Garage, on_delete=models.PROTECT, related_name="subscriptions")
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS, default="mpesa")
    payment = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.garage.name} subscription renewed"