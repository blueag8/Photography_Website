from django.conf.urls import url, include
from .views import all_services

urlpatterns = [
    url(r'^$', all_services, name='services'),
]