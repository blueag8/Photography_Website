from django.conf.urls import url, include
from products.views import all_products, image, portfolio, product, product_list
from django_filters.views import FilterView
from products.models import Product

urlpatterns = [
    url(r'^all_products/', all_products, name='products'),
    url(r'^portfolio/', portfolio, name='portfolio'),
    url(r'^product/(?P<id>\d+)', product, name='product'),
    url(r'^image/(?P<id>\d+)', image, name='image'),
    url(r'^list/', product_list, name='list')
    ]
