#urls.py
from django.contrib import admin
from django.urls import path

from .views import successView

urlpatterns = [
    path('price/', successView, name="price"),
]