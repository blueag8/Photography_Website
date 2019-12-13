from django.conf.urls import url, include
from authentication.views import index, logout, login, registration, ContactUs
from authentication import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^registration/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/', ContactUs, name="contact")
]
