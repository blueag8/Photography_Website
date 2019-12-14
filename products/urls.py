from django.conf.urls import url, include
from products.views import all_products, portfolio, product,image

urlpatterns = [
    url(r'^all_products/', all_products, name='products'),
    url(r'^portfolio/', portfolio, name='portfolio'),
    url(r'^product/(?P<id>\d+)', product, name='product'),
    url(r'^image/(?P<id>\d+)', image, name='image'),
    ]
