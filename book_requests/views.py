from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RequestForm

def request_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                "Collaboration request received! I endeavour to respond within 2 working days.")
    else:
        form = RequestForm()
    
    return render(request, 'book_requests/book_requests.html', {'form': form})
