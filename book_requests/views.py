from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RequestForm


def request_view(request):
    """
    Handle the display and processing of the book request form.

    This view handles both displaying the empty form (for GET requests)
    and processing form submissions (for POST requests).

    **Context:**
    - If the request method is POST, it processes the submitted form data.
      If the form is valid, it saves the request to the database and
      adds a success message for the user.
    - If the request method is GET, it simply displays an empty form.

    **Template:**
    - `book_requests/book_requests.html`

    **Messages:**
    - On successful form submission: "Book request received! I will try
    getting this loaded ASAP!"
    """
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Book request received! I will try getting this loaded ASAP!.")
    else:
        form = RequestForm()

    return render(request, 'book_requests/book_requests.html', {'form': form})
