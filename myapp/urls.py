from django.urls import path
from .views import *
urlpatterns =[
    path('',home, name ="home"),
    path('thank/',thank,name="thank"),
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

    path('mahindra1/',mahindra1,name='mahindra1'),
    path('mahindra2/',mahindra2,name='mahindra2'),
    path('mahindra3/',mahindra3,name='mahindra3'),
    path('mahindra4/',mahindra4,name='mahindra4'),
    
    path('tata1/',tata1,name='tata1'),
    path('tata2/',tata2,name='tata2'),
    path('tata3/',tata3,name='tata3'),
    path('tata4/',tata4,name='tata4'),

    path('royal1/',royal1,name='royal1'),
    path('royal2/',royal2,name='royal2'),

    path('tvs1/',tvs1,name='tvs1'),
    path('tvs2/',tvs2,name='tvs2'),

    path('revolt1/',revolt1,name='revolt1'),
    path('revolt2/',revolt2,name='revolt2'),

    path('ola1/',ola1,name='ola1'),

    path('tork1/',tork1,name='tork1')
            ]