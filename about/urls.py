#urls.py
from django.contrib import admin
from django.urls import path

from .views import about_view

urlpatterns = [
    path('', about_view, name="about"),
    path('/', about_view, name="about"),
    path('about/', about_view, name="about"),
]