from django.contrib import admin
from django.urls import path, include
from MLPL import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('module/', views.module, name='module'),
    
    
    path('operations/', include('operations.urls')),
]
