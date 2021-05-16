from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('add/', addpage, name='add_page'),
]