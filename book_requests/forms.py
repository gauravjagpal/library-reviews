from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'email', 'what_book_would_you_like_to_request']
