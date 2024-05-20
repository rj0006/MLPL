from django.contrib import admin
from django.urls import path
from master import views

urlpatterns = [
    path('', views.navbar, name='navbar'),
    
    path('state/', views.state, name='state'),
    path('statelist/', views.statelist, name='statelist'),
    path('updatestate/<id>', views.updatestate, name='updatestate'),
    path('deletestate/<id>/', views.deletestate, name='deletestate'),
    
    path('party/', views.party, name='party'),
    path('partylist/', views.partylist, name='partylist'),
    path('updateparty/<id>/', views.updateparty, name='updateparty'),
    path('deleteparty/<id>/', views.deleteparty, name='deleteparty'),
]