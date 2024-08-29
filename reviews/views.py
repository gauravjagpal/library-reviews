from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Book
from .forms import ReviewForm

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
    reviews = book.reviews.all()
    review_count = book.reviews.filter(approved=True).count()
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            reviews = review_form.save(commit=False)
            reviews.author = request.user
            reviews.book = book
            reviews.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )
            # Re-fetch all reviews after saving the new one
            reviews = book.reviews.all()
    review_form = ReviewForm()

    return render(
        request,
        "reviews/book_details.html",
        {
            "book": book,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )