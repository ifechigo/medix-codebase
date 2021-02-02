import django_filters

from .models import *


class MedicalFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = MedicalRecord
        fields = ['users', 'age', 'food_allergy','drug_allergy', 'tetanus_injection', 'malaria', 'fever', 'covid19', 'ebola', 'ulcer']
