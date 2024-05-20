from django.urls import path
from operations import views

urlpatterns = [
    path('', views.operation, name='operation'),
    path('consignment/', views.consignment, name='consignment'),
    path('get_ewaybill/', views.get_ewaybill, name='get_ewaybill'),
    path('consignment_tracking/', views.consignment_tracking, name='consignment-tracking'),
    
]
