import django_filters
from register.models import Building, Address
from django import forms

class BuildingFilter(django_filters.FilterSet):
 #   title = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.ModelMultipleChoiceFilter(queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple,lookup_expr='icontains')

    class Meta:
        model = Building
        fields = ['address']