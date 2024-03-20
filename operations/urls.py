from django.urls import path
from operations import views

urlpatterns = [
    path('', views.operation, name='operation'),
    path('consignment/', views.create_consignment_with_invoices, name='consignment_list'),
    
]
