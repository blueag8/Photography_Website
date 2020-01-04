from django.db import models
import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.models import CloudinaryField



# Create your models here.
class Product(models.Model):
       
    A4= 100
    A3= 150
    A3_Plus= 200

    size=[
    (A4,'A4 (21 x 29.7cm)'),
    (A3, 'A3 (29 x 42cm)'),
    (A3_Plus,'A3 + (32.9 x 48.3cm)'),
    ]
   
    size= models.IntegerField(choices=size, default='A4')
    price = models.IntegerField()
    category= models.CharField(max_length=100, default='')
    name = models.CharField(max_length=200, default = '')
    description = models.TextField()
    image = CloudinaryField('image', use_filename=True, unique_filename=False, folder='photography_website')



    def __str__(self):
        return self.name