from django_filters.rest_framework import FilterSet

from .models import Garage


class GarageFilter(FilterSet):
    
    class Meta:
        model = Garage
        fields = {
            'town': ['icontains', ]
        }
