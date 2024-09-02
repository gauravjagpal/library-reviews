"""
URL configuration for library_reviews project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("reviews.urls"), name="reviews-urls"),
    path("", include("book_requests.urls"), name="book_requests-urls"),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]
