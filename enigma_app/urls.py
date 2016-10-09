from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^enigma', views.enigma, name='enigma'),
    url(r'^encrypt', views.encrypt, name='encrypt'),
    url(r'^', views.home),
]
