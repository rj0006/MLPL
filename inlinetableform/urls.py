from django.contrib import admin
from django.urls import path, include
from inlinetableform import views

urlpatterns = [
    path('', views.inlinetable, name='inlinetable'),
    path('inlinelist/', views.inlinelist, name='inlinelist'),
    path('update/<authorid>/', views.update, name='update'), # <int:author_id>/
    path('delete/<authorid>/', views.delete, name='delete'),
    
    path('consignments/', views.consignments, name='consignments'),
]
