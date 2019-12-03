from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

    MONTH_CHOICES= [(i,i) for i in range (1,12)]
    YEAR_CHOICES=[(i,i) for i in range (2019,2040)]

    credit_card_number= forms.CharField(label="Card Number", required=False)
    name_on_card= forms.CharField(label="Name On Card", required=False)
    cvv = forms.CharField(label="Security (cvv) on back of card", required=False)
    expiry_month = forms.ChoiceField(label="Expiry Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Expiry Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.Form):

 
        CANVAS_SIZES=[ 
          ( 'A4', 'A4 = 21 x 29.7cm'),
          ( 'A3','A3 = 29 x 42cm'),
          ( 'A3+','A3 = 32.9 x 48.3cm'),
       ]
        Bool_choices=[
            (False, 'No'), 
            (True, 'Yes'),
        ]
        size = forms.ChoiceField(label="Canvas Size", widget=forms.Select, choices=CANVAS_SIZES)
        signed = forms.ChoiceField(label="signed", widget=forms.RadioSelect, choices=Bool_choices)
        class Meta:
                model = Order
                   
                fields = (
                   'full_name', 'email_address', 'phone_number', 'country', 'postcode', 
                   'town_or_city', 'street_address1', 'street_address2','county', 
        )

