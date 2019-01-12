from django.contrib import admin
from django.urls import path

from .views import all_gallery_view, detail_gallery_view

urlpatterns = [
    path('gallery/', all_gallery_view, name="gallery"),
    path('gallery/<int:id>', detail_gallery_view, name="gallery")
]
