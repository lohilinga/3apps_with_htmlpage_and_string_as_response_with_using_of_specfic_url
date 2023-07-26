app_name='second'
from django.urls import path
from app2.views import *
urlpatterns =[
    path('four/',four,name='four'),
    path('five/',five,name='five'),
    path('six/',six,name='six'),
]
