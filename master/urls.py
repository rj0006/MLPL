from django.contrib import admin
from django.urls import path
from master import views

urlpatterns = [
    path('', views.navbar, name='navbar'),
    path('party/', views.party, name='party'),
    path('partylist/', views.partylist, name='partylist'),
    path('updateparty/<id>/', views.updateparty, name='updateparty'),
    path('deleteparty/<id>/', views.deleteparty, name='deleteparty'),
]