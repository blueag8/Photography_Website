from django.test import TestCase
from .models import Order

# Test Order Form

class OrderForm(TestCase):

        class Meta:
                model = Order
                fields = (
                   'full_name', 'email_address', 'phone_number', 'country', 'postcode', 
                   'town_or_city', 'street_address1', 'street_address2',
        )