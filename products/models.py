from django.db import models

# Create your models here.
class Product(models.Model):
    CANVAS_SIZES=[ 
          ( 'A4', 'A4 = 21 x 29.7cm'),
          ( 'A3','A3 = 29 x 42cm'),
          ( 'A3+','A3 = 32.9 x 48.3cm'),
       ]
    Bool_choices=[
            (False, 'No'), 
            (True, 'Yes'),
        ]

    name = models.CharField(max_length=200, default = '')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    size = models.CharField(max_length=20, choices=CANVAS_SIZES, default="A4")
    signed = models.BooleanField(choices=Bool_choices, default=True ) 


    def __str__(self):
        return self.name