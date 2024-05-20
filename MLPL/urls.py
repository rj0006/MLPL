from django.contrib import admin
from django.urls import path, include
from MLPL import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login_page'),
    path('module/', views.module, name='module'),
    path('administrations/', include('administrations.urls')),
    path('accounts/', include('accounts.urls')),
    path('master/', include('master.urls')),
    
    path('operations/', include('operations.urls')),
    path('chatApp/', include('chatApp.urls')),
    path('inlinetableform/', include('inlinetableform.urls')),
]
urlpatterns += staticfiles_urlpatterns()

