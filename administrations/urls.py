from django.urls import path
from administrations import views

urlpatterns = [
    path('', views.navbar, name='navbar'),
    path('users/', views.users, name='users'),
    path('usersList/', views.usersList, name='usersList'),
    path('get_party_list/', views.get_party_list, name='get_party_list')
]
