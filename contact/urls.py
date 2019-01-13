from django.contrib import admin
from django.urls import path

from .views import email_view, success_view

urlpatterns = [
    path('contact/', email_view, name='contact'),
    path('contact/success/', success_view, name='success'),
]