from django.db import models
from apps.core.models import AbstractBaseModel, CarBrand
from django.conf import settings
# Create your models here.


GENDER_TYPES = (
    ("female", "Female"),
    ("male", "Male"),
    ("other", "Other"),
)

MARITAL_STATUS_CHOICES = (
    ("single", "Single"),
    ("married", "Married"),
    ("divorced", "Divorced"),
    ("widowed", "Widowed"),
)

class Driver(AbstractBaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True, blank=True)
    kra_pin = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_TYPES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(AbstractBaseModel):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="cars")
    number_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT)
    car_model = models.CharField(max_length=255, null=True, blank=True)
    year_manufactured = models.CharField(max_length=4, null=True, blank=True)
    
    engine_capacity = models.FloatField(default=0)

    def __str__(self):
        return self.number_plate