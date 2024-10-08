from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Reviewed
from .forms import ReviewForm


# Create your views here.
class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.all().order_by("id")
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
            review = review_form.save(commit=False)
            review.author = request.user
            review.book = book

            if request.user.is_staff:
                # Automatically approved if the user is an admin
                review.approved = True
                messages.add_message(
                    request, messages.SUCCESS,
                    'Review submitted and approved!'
                )
            else:
                # Review goes to admin to approve if the user is not staff
                review.approved = False
                messages.add_message(
                    request, messages.SUCCESS,
                    'Review submitted and awaiting approval'
                )

            review.save()

            # Re-fetch all reviews after saving the new one
            reviews = book.reviews.all()

    review_form = ReviewForm()

    return render(request, 'reviews/book_details.html', {
        'book': book,
        'reviews': reviews,
        'review_count': review_count,
        'review_form': review_form
    })


def review_edit(request, slug, review_id):
    """
    View to edit reviews
    """
    if request.method == "POST":

        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Reviewed, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.book = book

            # Automatically approved if the user is an admin
            if request.user.is_staff:
                review.approved = True
                messages.add_message(request, messages.SUCCESS,
                                     'Review updated and approved!')
            else:
                # Edited review goes to admin to approve if user is not staff
                review.approved = False
                messages.add_message(request, messages.SUCCESS,
                                     'Review updated, approval pending!')

            review.save()
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating review!')

    return HttpResponseRedirect(reverse('book_details', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Reviewed, pk=review_id)

# If user is the author they can delete their own review
    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own review!')

    return HttpResponseRedirect(reverse('book_details', args=[slug]))
