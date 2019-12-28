from django.shortcuts import get_object_or_404
from products.models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):
    price=django_filters.RangeFilter()
    
    
    class Meta:
       model = Product
       fields = ['price']
     

    