from django.urls import path
from . import views
"""
URL configuration for library_reviews project.

The `urlpatterns` list routes URLs to views.
"""

urlpatterns = [
    path('book_requests.html', views.request_view, name='book_requests'),
]
