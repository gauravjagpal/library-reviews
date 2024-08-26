from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 6