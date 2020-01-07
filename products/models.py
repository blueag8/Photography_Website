from django.db import models
import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.models import CloudinaryField



# Create your models here.
class Product(models.Model):
       
    price = models.IntegerField()
    category= models.CharField(max_length=100, default='')
    name = models.CharField(max_length=200, default = '')
    description = models.TextField()
    image = CloudinaryField('image', use_filename=True, unique_filename=False, folder='photography_website')



    def __str__(self):
        return self.name
