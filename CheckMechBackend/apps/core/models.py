from django.db import models

# Create your models here.
FUEL_TYPES = (
    ("petrol", "Petrol"),
    ("diesel", "Diesel"),
    ("electric", "Electric"),
    ("hybrid", "Hybrid"),
)

class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CarBrand(AbstractBaseModel):
    name = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255, choices=FUEL_TYPES)

    def __str__(self):
        return self.name