from django.conf.urls import url
from .views import contactUs


urlpatterns = [
    url(r'^$', contactUs, name="contactUs")
]