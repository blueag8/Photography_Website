from django.db import models
import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.models import CloudinaryField



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default = '')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', use_filename=True, unique_filename=False, folder='photography_website')



    def __str__(self):
        return self.name