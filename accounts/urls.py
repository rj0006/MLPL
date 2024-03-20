# urls.py
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.navbar, name='navbar'),
    path('bill-journal/', views.bill_journal, name='bill_journal'),

    # http://127.0.0.1:8000/accounts/get_names/?search=har (har is search key)
    path('get_names/', views.get_names, name='get_names'),

    # Add other URL patterns as needed
]
