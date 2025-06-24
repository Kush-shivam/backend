from django.urls import path
from .views import *
urlpatterns =[
    path('',home, name ="home"),
    path('contact/',contact, name="contact"),
    path('about/',about, name="about"),
    path('bike/',bike, name="bike"),
    path('car/',car, name="car"),
    path('mahindra/',mahindra, name="mahindra"),
    path('ola/',ola, name="ola"),
    path('revolt/',revolt, name='revolt'),
    path('royal/',royal, name='royal'),
    path('tata/',tata, name='tata'),
    path('tork/',tork, name='tork'),
    path('tvs/',tvs, name='tvs'),
            ]