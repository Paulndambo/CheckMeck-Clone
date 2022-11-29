from django.contrib import admin
from .models import Garage, GarageSubscription, Service
# Register your models here.
admin.site.register(Garage)
admin.site.register(GarageSubscription)
admin.site.register(Service)
