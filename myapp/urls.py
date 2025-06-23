from django.urls import path
from .views import *
urlpatterns =[
    path('',home, name ="home"),
    path('index/',home, name ="home"),
    path('contact/',contact, name="contact"),
    path('about/',about,name="about"),
    path('bike/',bike,name="bike"),
    path('car/',car,name="car"),
    path('mahindra/',mahindra,name="mahindra"),
            ]