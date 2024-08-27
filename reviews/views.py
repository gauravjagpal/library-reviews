from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book

# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 6


def book_details(request, slug):
    """
    Display an individual :model:`reviews.Book`.

    **Context**

    ``book``
        An instance of :model:`reviews.Book`.

    **Template:**

    :template:`reviews/book_details.html`
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "reviews/book_details.html",
        {"book": book},
    )