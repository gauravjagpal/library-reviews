from django.urls import path
from . import views


urlpatterns = [
    path('book_requests.html', views.request_view, name='book_requests'),
]
