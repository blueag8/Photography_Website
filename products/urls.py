from django.conf.urls import url, include
from products.views import all_products, portfolio

urlpatterns = [
    url(r'^all_products/', all_products, name='products'),
    url(r'^portfolio/', portfolio, name='portfolio'),

]