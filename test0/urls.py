from django.urls import path
from . import view

urlpatterns = [
    path( '' , view.homepage , name='home' ),
    path( 'reto/' , view.reto , name='reto' ),
    path( 'count/' , view.count , name='count'),

    #path('passInfo/',view.homepage2),
    #path('hello/',view.hello),
    #path('marco/',view.marco),
]
