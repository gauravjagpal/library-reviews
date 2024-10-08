from . import views
from django.urls import path
"""
URL configuration for library_reviews project.

The `urlpatterns` list routes URLs to views.
"""
urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<slug:slug>/', views.book_details, name="book_details"),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
