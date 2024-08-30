from .models import Reviewed
from django import forms
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviewed
        fields = ('body',)