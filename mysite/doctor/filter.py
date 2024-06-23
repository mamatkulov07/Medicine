from django_filters.rest_framework import FilterSet
from .models import Doctor


class MovieFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'education',
            'hospital',
            'specialty',
        }