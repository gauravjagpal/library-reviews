from .models import Reviewed
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviewed
        fields = ('body',)