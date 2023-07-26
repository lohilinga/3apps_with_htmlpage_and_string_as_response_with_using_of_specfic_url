app_name='three'
from django.urls import path
from app3.views import *
urlpatterns = [
    path('seven/',seven,name='seven'),
    path('eight/',eight,name='eight'),
    path('nine/',nine,name='nine')
]