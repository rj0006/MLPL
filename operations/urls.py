from django.urls import path, include
from operations.views import *

urlpatterns = [
    path('consignment/', index, name='index'),
]
