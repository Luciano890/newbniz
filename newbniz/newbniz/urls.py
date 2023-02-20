"""Urls for newbniz project."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('derivatives/', include('derivatives.urls')),
    path('functions/', include('functions.urls')),
    path('integrals/', include('integrals.urls')),
]
