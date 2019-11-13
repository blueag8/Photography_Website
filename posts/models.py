from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200, default = '')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title


